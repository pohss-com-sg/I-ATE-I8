from flask import *
from gemini import bot, meal_plan_spilt, roles#you can use the functions bot(bot_role), roles(number) !!IMPT!!
# import spinx #for the recongintion AI and go the google translate
#from fileinput import filename #if we ever do food detection

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite///test.db"

api_key = ""
instruction = ""


@app.route("/")
def index():
    #When clicked goes to main page
    return render_template("index.html")

@app.route("/chatbot")
def chatbot():
    #When clicked goes to chat bot page
    return render_template("chatbot.html")

@app.route("/mealplan")
def mealplan():
    #When clicked goes to meal planning page
    return render_template("mealplan.html")

@app.route("/translate")
def translate():
    #When clicked goes to translating page
    return render_template("translate.html")

@app.route("/db")
def db():
    #When clicked goes to database page
    return render_template("fooddb.html")

@app.route("/text-input1", methods=["GET", "POST"])
def text_input1():
    #WHEN THE FORM IS SUBMITTED IT WILL RECIEVE IT
    #WE WILL USE THIS FOR CHATBOT AND MEAL PLANNER
    if request.method == "POST":
        text = request.form["text"]
        print(text)
        bot_role = roles(1)
        personality = bot_role[0] 
        type = bot_role[1]
        response = bot(bot_role, type)
        return render_template("index.html")
        #RETURN CALL AI FUNCTION AND REUTRN OUTPUT AND GET

@app.route("/text-input2", methods=["GET", "POST"])
def text_input2():
    #WHEN THE FORM IS SUBMITTED IT WILL RECIEVE IT
    #WE WILL USE THIS FOR CHATBOT AND MEAL PLANNER
    if request.method == "POST":
        text = request.form["text"]
        print(text)
        bot_role = roles(2)
        personality = bot_role[0] 
        type = bot_role[1]
        response = bot(bot_role, type)
        
        return render_template("index.html")
        #RETURN CALL AI FUNCTION AND REUTRN OUTPUT AND GET

if __name__ == "__main__":
    #runs the app / website
    app.run(debug=True)

#http://127.0.0.1:5000