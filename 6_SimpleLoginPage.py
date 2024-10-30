#6. Simple Login Page

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "user" and password == "password":
            message = "Welcome User!"
        else:
            message = "Invalid username or password. Please try again."
    return render_template("login.html", message=message)
if __name__ == "__main__":
    app.run(debug=True)
