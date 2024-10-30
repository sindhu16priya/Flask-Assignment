#10. Temperature Converter

from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/convert", methods=["GET","POST"])
def convert():
    result = None
    if request.method=="POST":
        try:
            celsius=float(request.form["celsius"].strip().replace(",","."))
            result=(celsius*9/5)+32
        except ValueError:
            result="Invalid input"
    return render_template("temperature.html",result=result)
if __name__ == "__main__":
    app.run(debug=True)

