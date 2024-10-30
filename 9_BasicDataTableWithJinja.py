#9. Basic Data Table with Jinja

from flask import Flask, render_template
app = Flask(__name__)
users = [
    {"name": "Sindhu", "age": 21, "city": "Hyderabad"},
    {"name": "Priya", "age": 24, "city": "Kolkata"},
    {"name": "Aarav", "age": 30, "city": "Mumbai"},
    {"name": "Lakshmi", "age": 24, "city": "Chennai"},
    {"name": "Ekaksh", "age": 29, "city": "Delhi"},
    {"name": "Supriya", "age": 35, "city": "Bengaluru"},
    {"name": "Ram", "age": 27, "city": "Hyderabad"}
]
@app.route("/users")
def users_table():
    return render_template("table.html", users=users)
if __name__ == "__main__":
    app.run(debug=True)
