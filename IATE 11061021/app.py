from flask import *
from fileinput import filename

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite///test.db"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

@app.route("/mealplan")
def mealplan():
    return render_template("mealplan.html")

@app.route("/translate")
def translate():
    return render_template("translate.html")

if __name__ == "__main__":
    app.run(debug=True)