import sqlite3 as sql
import time
import secrets
import html

from werkzeug.security import generate_password_hash, check_password_hash

def insertUser(username, password, DoB):
    con = sql.connect("database_files/database.db")
    cur = con.cursor()

    #Hash password before storing it in the database to improve security
    hashed_password = generate_password_hash(password)

    cur.execute(
        "INSERT INTO users (username,password,dateOfBirth) VALUES (?,?,?)",
        (username, hashed_password, DoB),
    )
    con.commit()
    con.close()


def retrieveUsers(username, password):
    con = sql.connect("database_files/database.db")
    cur = con.cursor()

    # Only retireve hashed passwords for the given username
    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    result = cur.fetchone()
    
    if result is None:
        con.close()
        return False
    stored_password = result[0]
    # Compare the provided password with the stored hashed password using check_password_hash
    if not check_password_hash(stored_password, password):
        con.close()
        return False    

    # Safer file handling for visitor count log as requested by Unsecure PWA management
    try:
        with open("visitor_log.txt", "r") as file:
            number = int(file.read().strip())
    except:
         number = 0 #File might not exist yet, so we start with 0
    number += 1

    # Controlled write to file   
    with open("visitor_log.txt", "w") as file:
            file.write(str(number))

        #Secure random delay to mitigate timing attacks as requested by Unsecure PWA management
    time.sleep(secrets.randbelow(11) / 1000 + 0.08)
    con.close()
    return True


def insertFeedback(feedback):
    con = sql.connect("database_files/database.db")
    cur = con.cursor()
    # Fixed parameterised query to prevent SQL injection and XSS attacks
    cur.execute("INSERT INTO feedback (feedback) VALUES (?)", (feedback,))
    con.commit()
    con.close()


def listFeedback():
    con = sql.connect("database_files/database.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM feedback").fetchall()
    con.close()


    # Safer file handling for feedback display as requested by Unsecure PWA management
    with open("templates/partials/success_feedback.html", "w") as f:
        for row in data:
            f.write("<p>\n")

        # Escape feedback to prevent XSS attacks
        safe_feedback = html.escape(row[1])
        f.write(f"{safe_feedback}\n")
        f.write("</p>\n")
