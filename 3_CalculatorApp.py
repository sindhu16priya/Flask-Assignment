#3. Calculator App

from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/calculator")
def calculator():
    return render_template("calculator.html", result=None)
@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        n1=float(request.form["n1"])
        n2=float(request.form["n2"])
        result=n1+n2
    except ValueError:
        result="Invalid input"
    return render_template("calculator.html",result=result)
if __name__ == "__main__":
    app.run(debug=True)
