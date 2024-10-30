#8. Feedback Form

from flask import Flask, render_template, request
app = Flask(__name__)
feedback_list=[]
@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method=="POST":
        name=request.form.get("name")
        feedback=request.form.get("feedback")
        if name and feedback:
            feedback_list.append({"name":name,"feedback":feedback})   
    return render_template("feedback.html", feedback_list=feedback_list)
if __name__ == "__main__":
    app.run(debug=True)
