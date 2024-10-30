#4. Mini To-Do List

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
tasks = []
@app.route("/todo")
def todo():
    return render_template("todo.html", tasks=tasks)
@app.route("/add_task", methods=["POST"])
def add_task():
    task = request.form["task"]
    tasks.append(task)
    return redirect(url_for("todo"))
if __name__ == "__main__":
    app.run(debug=True)
