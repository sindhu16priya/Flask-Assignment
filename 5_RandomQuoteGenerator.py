#5. Random Quote Generator

from flask import Flask, render_template
import random
app = Flask(__name__)
quotes = [
    "The only way to do great work is to love what you do. — Steve Jobs",
"Success is not final, failure is not fatal: It is the courage to continue that counts. — Winston Churchill" ,
"Don't watch the clock; do what it does. Keep going. — Sam Levenson",
"Believe you can and you're halfway there. — Theodore Roosevelt",
"I find that the harder I work, the more luck I seem to have.— Thomas Jefferson",
"What lies behind us and what lies before us are tiny matters compared to what lies within us. — Ralph Waldo Emerson",
"It does not matter how slowly you go as long as you do not stop. — Confucius",
"You miss 100% of the shots you don’t take. — Wayne Gretzky",
"Whether you think you can or you think you can't, you're right. — Henry Ford",
"The best way to predict your future is to create it. — Peter Drucker"
]
@app.route("/quote")
def quote():
    random_quote = random.choice(quotes)
    return render_template("quote.html", quote=random_quote)
if __name__ == "__main__":
    app.run(debug=True)
