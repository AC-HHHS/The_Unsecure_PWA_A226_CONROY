# Broken Authentication and Session Management

Many websites require users to log in to access their data or engage with the website services, etc. More often than not, this is done using a username and password. With this information, a site will assign and send each logged-in visitor a unique session ID that serves as a key to the user’s identity on the server.

When these bedrock systems are "broken," threat actors can easily exploit them. This vulnerability is extremely broad in nature, with multiple attack vectors, including dictionary attacks, XSS/XFS, side-channel attacks, SQL injections, and most types of phishing.

## Common examples of broken authentication and session management

1. Weak or [Common passwords](https://github.com/danielmiessler/SecLists/tree/master/Passwords) are allowed allowing dictionary brute force attacks
2. Weak or ineffective credential recovery/forgot-password processes, which can be easily brute-forced.
3. Exposed session IDs or session IDs that can be calculated or brute-forced
4. Persistent session IDs are not properly invalidated during logout or a period of inactivity.
5. When re-authentication is not required for administrative or destructive processes
6. Inappropriate caching of session IDs
7. Predictable authentication tokens

## How to penetrate test for this vulnerability

1. Try to create a new user with simple or [Common passwords](https://github.com/danielmiessler/SecLists/tree/master/Passwords).
2. Write a script or a pen-testing application to brute force [Common passwords](https://github.com/danielmiessler/SecLists/tree/master/Passwords) and [common usernames](https://github.com/danielmiessler/SecLists/tree/master/Usernames).
3. Log out, and then try navigating to URLs that require authentication.
4. If the application uses cookies to manage sessions, try copying the cookies to a different computer and see if the session persists.
5. Analyse cookies for patterns that could be reverse-engineered or brute-forced.

## How to countermeasure this vulnerability

1. Enforce strong passwords
2. [Log](..\defensive_data_handling\README.md#Logging) all failed login attempts and implement a failed login policy. For example, when multiple failed login attempts are detected from the same IP address or same username.
3. Implement a secure, server-side session management system that creates a new, random session ID with high complexity each time someone logs in. Ensure the session ID is not visible in the web page's URL, is kept safe, and is properly discarded following a user's logout, periods of inactivity, or after session timeouts. For example, install and configure [Flask Session](https://flask-session.readthedocs.io/en/latest/)
4. Implement [two-factor authentication](.student_resources\two_factor_authentication).
5. Conduct regular [security audits and testing](.student_resources\security_testing_approaches).
6. Implement strong rate limiting for a login page. For example, install and configure [Flask Limiter](https://flask-limiter.readthedocs.io/en/stable/)
