from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from waitress import serve
import user_management as dbHandler

# Code snippet for logging a message
# app.logger.critical("message")

app = Flask(__name__)

# List of allowed URLs for redirection to prevent open redirect vulnerabilities
ALLOWED_URLS = ["/", "/index.html", "/signup.html", "/success.html"]

def safe_redirect(url):
    if url in ALLOWED_URLS:
        return redirect(url)
    else:
        return redirect("/")


@app.route("/success.html", methods=["POST", "GET", "PUT", "PATCH", "DELETE"])
def addFeedback():
    #Validate redirect URL
    if request.method == "GET" and request.args.get("url"):
        url = request.args.get("url", "")
        return safe_redirect(url)
    
    if request.method == "POST":
        feedback = request.form["feedback"]
        # input validation for feedback to prevent XSS attacks
        if not feedback or len(feedback) > 500:
            return render_template("/success.html", state=False, value="Invalid input")  
        
        dbHandler.insertFeedback(feedback)
        dbHandler.listFeedback()
        return render_template("/success.html", state=True, value="Back")
    else:
        dbHandler.listFeedback()
        return render_template("/success.html", state=True, value="Back")


@app.route("/signup.html", methods=["POST", "GET", "PUT", "PATCH", "DELETE"])
def signup():
    if request.method == "GET" and request.args.get("url"):
        url = request.args.get("url", "")
        return safe_redirect(url)
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        DoB = request.form["dob"]

        # Basic input validation
        if not username or not password:
            return render_template("/signup.html")
        
        dbHandler.insertUser(username, password, DoB)
        return render_template("/index.html")
    else:
        return render_template("/signup.html")


@app.route("/index.html", methods=["POST", "GET", "PUT", "PATCH", "DELETE"])
@app.route("/", methods=["POST", "GET"])
def home():
    #Using Safe redirect
    if request.method == "GET" and request.args.get("url"):
        url = request.args.get("url", "")
        return safe_redirect(url)
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # Input validation for login credentials
        if not username or not password:
            return render_template("/index.html")


        isLoggedIn = dbHandler.retrieveUsers(username, password)
        if isLoggedIn:
            dbHandler.listFeedback()
            return render_template("/success.html", value=username, state=isLoggedIn)
        else:
            return render_template("/index.html")
    else:
        return render_template("/index.html")


if __name__ == "__main__":
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
    # Using waitress instead of Flask's debug
    # Local Host binding improves security
    serve(app, debug=False, host="127.0.0.1", port=5000)
