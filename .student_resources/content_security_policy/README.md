# Content Security Policy

Content Security Policy (CSP) can significantly reduce the risk and impact of cross-site scripting attacks in modern browsers. A CSP has been a W3C recommendation since 2016 and is now the industry standard in securing web applications.

More information on CSP: [w3c documentation](http://www.w3.org/TR/CSP2/)

## To add a Content Security Policy header to your Flask application

### Design your policy

Students can either follow the CSP documentation to design their policy or they can use a [CSP generator](https://www.validbot.com/tools/csp-wizard.php).

### Installation

Install the extension using pip or easy_install. [Pypi Link](https://pypi.python.org/pypi/flask-csp)

```bash
$ pip install flask-csp
```

## Usage

Add the csp_header(...) decorator after the app.route(...) decorator to create a csp header on each route. The decorator can either be passed no value (Add default policies) or custom values by a dict (Add custom policies). For more information on the default policies, see "Change Default Policies" below.

### Add default header

```python
    @app.route('/', methods=['POST', 'GET'])
    @app.route('/index.html', methods=['GET'])
    @csp_header({
        "base-uri": "self",
        "default-src": "'self'",
        "style-src": "'self'",
        "script-src": "'self'",
        "img-src": "*",
        "media-src": "'self'",
        "font-src": "self",
        "object-src": "'self'",
        "child-src": "'self'",
        "connect-src": "'self'",
        "worker-src": "'self'",
        "report-uri": "/csp_report",
        "frame-ancestors": "'none'",
        "form-action": "'self'",
        "frame-src": "'none'",
    })
    def index():
        #index implementation

#report ant CSP violations to the system log.
@app.route("/csp_report", methods=["POST"])
@csrf.exempt
def csp_report():
    app.logger.critical(request.data.decode())
    return "done"
```

### Add a match CSP meta head to the `layout.html` template.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta
      http-equiv="Content-Security-Policy"
      content="base-uri 'self'; default-src 'self'; style-src 'self'; script-src 'self'; img-src 'self' *; media-src 'self'; font-src 'self'; connect-src 'self'; object-src 'self'; worker-src 'self'; frame-src 'none'; form-action 'self'; manifest-src 'self'"
    />
    <meta charset="utf-8" />
  </head>
</html>
```
