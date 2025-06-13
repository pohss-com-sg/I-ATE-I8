from flask import Flask, render_template, request, jsonify
from gemini import bot, roles#you can use the functions bot(bot_role), roles(number) !!IMPT!!
from ast import literal_eval
# import spinx #for the recongintion AI and go the google translate
#from fileinput import filename #if we ever do food detection
#wanted to use sql but didnt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"


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

@app.route("/db")
def db():
    #When clicked goes to database page
    return render_template("fooddb.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json(force=True)
        if not data:
             return jsonify({"response": "Error: No JSON data received."}), 400

        user_msg = data.get("message", "")
        role_type = data.get("role", "chat")

        if not user_msg:
             return jsonify({"response": "Error: No message provided."}), 400

        # ASSIGNS THE ROLE OF THE PERSONALITY LJ
        bot_role = roles(1)
        # print(bot_role)
        personality = bot_role[0]
        type = bot_role[1]

        # combo history
        response = bot(personality, type, user_msg)

        return jsonify({"response": response})
    except Exception as e:
         print("Execution in /ask:", e)
         return jsonify({"response": "Internal server error."}), 500
    
# @app.route("/text-input1", methods=["GET", "POST"])
# def text_input1():
#     #WHEN THE FORM IS SUBMITTED IT WILL RECIEVE IT
#     #WE WILL USE THIS FOR CHATBOT AND MEAL PLANNER
#     if request.method == "POST":
#         text = request.form.get("text", "")
#         print(text)
#         bot_role = roles(1)
#         personality = bot_role[0] 
#         type = bot_role[1]
#         response = bot(bot_role, "chat", user_msg)
#         return render_template("index.html")
#         #RETURN CALL AI FUNCTION AND REUTRN OUTPUT AND GET
#SS WILL DO PART 1 so change og plan

def meal_plan_spilt(response):
            #type == type of bot e.g chat/plan, response is gemini's response
            #DO SPLITING OF DICTIONARIES AND PUT AS A LIST AND SEND IT TO THE AP

            responselist = response.strip('```python').strip('```').strip()
            responselist = literal_eval(responselist)
            # print(responselist)
            Dates = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
            bld = ["BREAKFAST","LUNCH","DINNER"]
            inbld = ["name", "ingredients", "recipe"]
            #goofy ah hard coding but it works 
            # Monday
            mb = f"BREAKFAST FOOD NAME: {responselist[Dates[0]][bld[0]][inbld[0]]} <br> INGREDIENTS NEEDED: {', '.join(responselist[Dates[0]][bld[0]][inbld[1]])} <br> RECIEPE: {', '.join(responselist[Dates[0]][bld[0]][inbld[2]])} <br>"
            ml = f"LUNCH FOOD NAME: {responselist[Dates[0]][bld[1]][inbld[0]]} <br> INGREDIENTS NEEDED: {',' .join(responselist[Dates[0]][bld[1]][inbld[1]])} <br> RECIEPE: {', '.join(responselist[Dates[0]][bld[1]][inbld[2]])} <br>"
            md = f"DINNER FOOD NAME: {responselist[Dates[0]][bld[2]][inbld[0]]} <br> INGREDIENTS NEEDED: {',' .join(responselist[Dates[0]][bld[2]][inbld[1]])} <br> RECIEPE: {', '.join(responselist[Dates[0]][bld[2]][inbld[2]])} <br>"

            # Tuesday
            tub = f"BREAKFAST FOOD NAME: {responselist[Dates[1]][bld[0]][inbld[0]]} <br> INGREDIENTS NEEDED: {', '.join(responselist[Dates[1]][bld[0]][inbld[1]])} <br>  RECIEPE: {', '.join(responselist[Dates[1]][bld[0]][inbld[2]])} <br>"
            tul = f"LUNCH FOOD NAME: {responselist[Dates[1]][bld[1]][inbld[0]]} <br> INGREDIENTS NEEDED: {', '.join(responselist[Dates[1]][bld[1]][inbld[1]])} <br>  RECIEPE: {', '.join(responselist[Dates[1]][bld[1]][inbld[2]])} <br>"
            tud = f"DINNER FOOD NAME: {responselist[Dates[1]][bld[2]][inbld[0]]} <br> INGREDIENTS NEEDED: {', '.join(responselist[Dates[1]][bld[2]][inbld[1]])} <br> RECIEPE: {', '.join(responselist[Dates[1]][bld[2]][inbld[2]])} <br>"

            # Wednesday
            wb = f"BREAKFAST FOOD NAME: {responselist[Dates[2]][bld[0]][inbld[0]]} <br> INGREDIENTS NEEDED: {', '.join(responselist[Dates[2]][bld[0]][inbld[1]])} <br> RECIEPE: {', '.join(responselist[Dates[2]][bld[0]][inbld[2]])} <br>"
            wl = f"LUNCH FOOD NAME: {responselist[Dates[2]][bld[1]][inbld[0]]} <br> INGREDIENTS NEEDED: {', '.join(responselist[Dates[2]][bld[1]][inbld[1]])} <br> RECIEPE: {', '.join(responselist[Dates[2]][bld[1]][inbld[2]])} <br>"
            wd = f"DINNER FOOD NAME: {responselist[Dates[2]][bld[2]][inbld[0]]} <br> INGREDIENTS NEEDED: {', '.join(responselist[Dates[2]][bld[2]][inbld[1]])} <br> RECIEPE: {', '.join(responselist[Dates[2]][bld[2]][inbld[2]])} <br>"

            # Thursday
            thb = f"BREAKFAST FOOD NAME: {responselist[Dates[3]][bld[0]][inbld[0]]} <br> INGREDIENTS NEEDED: {', '.join(responselist[Dates[3]][bld[0]][inbld[1]])} <br> RECIEPE: {', '.join(responselist[Dates[3]][bld[0]][inbld[2]])} <br>"
            thl = f"LUNCH FOOD NAME: {responselist[Dates[3]][bld[1]][inbld[0]]} <br> INGREDIENTS NEEDED: {', '.join(responselist[Dates[3]][bld[1]][inbld[1]])} <br> RECIEPE: {', '.join(responselist[Dates[3]][bld[1]][inbld[2]])} <br>"
            thd = f"DINNER FOOD NAME: {responselist[Dates[3]][bld[2]][inbld[0]]} <br> INGREDIENTS NEEDED: {', '.join(responselist[Dates[3]][bld[2]][inbld[1]])} <br> RECIEPE: {', '.join(responselist[Dates[3]][bld[2]][inbld[2]])} <br>"

            # Friday
            fb = f"BREAKFAST FOOD NAME: {responselist[Dates[4]][bld[0]][inbld[0]]} <br> INGREDIENTS NEEDED: {', '.join(responselist[Dates[4]][bld[0]][inbld[1]])} <br> RECIEPE: {', '.join(responselist[Dates[4]][bld[0]][inbld[2]])} <br>"
            fl = f"LUNCH FOOD NAME: {responselist[Dates[4]][bld[1]][inbld[0]]} <br> INGREDIENTS NEEDED: {', '.join(responselist[Dates[4]][bld[1]][inbld[1]])} <br> RECIEPE: {', '.join(responselist[Dates[4]][bld[1]][inbld[2]])} <br>"
            fd = f"DINNER FOOD NAME: {responselist[Dates[4]][bld[2]][inbld[0]]} <br> INGREDIENTS NEEDED: {', ' .join(responselist[Dates[4]][bld[2]][inbld[1]])} <br> RECIEPE: {', '.join(responselist[Dates[4]][bld[2]][inbld[2]])} <br>"

            # Saturday
            satb = f"BREAKFAST FOOD NAME: {responselist[Dates[5]][bld[0]][inbld[0]]} <br> INGREDIENTS NEEDED: {', '.join(responselist[Dates[5]][bld[0]][inbld[1]])} <br> RECIEPE: {', '.join(responselist[Dates[5]][bld[0]][inbld[2]])} <br>"
            satl = f"LUNCH FOOD NAME: {responselist[Dates[5]][bld[1]][inbld[0]]} <br> INGREDIENTS NEEDED: {', '.join(responselist[Dates[5]][bld[1]][inbld[1]])} <br> RECIEPE: {', '.join(responselist[Dates[5]][bld[1]][inbld[2]])} <br>"
            satd = f"DINNER FOOD NAME: {responselist[Dates[5]][bld[2]][inbld[0]]} <br> INGREDIENTS NEEDED: {', '.join(responselist[Dates[5]][bld[2]][inbld[1]])} <br> RECIEPE: {', '.join(responselist[Dates[5]][bld[2]][inbld[2]])} <br>"

            # Sunday
            sunb = f"BREAKFAST FOOD NAME: {responselist[Dates[6]][bld[0]][inbld[0]]} <br> INGREDIENTS NEEDED: {', '.join(responselist[Dates[6]][bld[0]][inbld[1]])} <br> RECIEPE: {', '.join(responselist[Dates[6]][bld[0]][inbld[2]])}<br>"
            sunl = f"LUNCH FOOD NAME: {responselist[Dates[6]][bld[1]][inbld[0]]} <br> INGREDIENTS NEEDED: {', '.join(responselist[Dates[6]][bld[1]][inbld[1]])} <br> RECIEPE: {', '.join(responselist[Dates[6]][bld[1]][inbld[2]])} <br>"
            sund = f"DINNER FOOD NAME: {responselist[Dates[6]][bld[2]][inbld[0]]} <br> INGREDIENTS NEEDED: {', '.join(responselist[Dates[6]][bld[2]][inbld[1]])} <br> RECIEPE: {', '.join(responselist[Dates[6]][bld[2]][inbld[2]])} <br>"
            
            return mb, ml, md, tub, tul, tud, wb, wl, wd, thb, thl, thd, fb, fl, fd, satb, satl, satd, sunb, sunl, sund

@app.route("/text-input2", methods=["GET", "POST"])
def text_input2():
    #WHEN THE FORM IS SUBMITTED IT WILL RECIEVE IT
    #WE WILL USE THIS FOR CHATBOT AND MEAL PLANNER
    #FIX EMPTY LIST WILL GIVE ERROR!!!!
    if request.method == "POST":
        prompt = request.form["text"]
        if not prompt:  # Check if the prompt is empty
            return render_template("mealplan.html", error="Input cannot be empty.")
        print(prompt)
        bot_role = roles(2)
        # print(bot_role + "dewreggewrhgewrgrefwdsf")
        personality = bot_role[0]
        type = bot_role[1]
        # combo history
        try:
            response = bot(personality, type, prompt) 
        except Exception as e:
            print(f"Error processing bot response: {e}")
            return render_template("mealplan.html", error="An error occurred while processing your input. Please try again.") 
        #get dict from gemini
        #THIS IS SO INEFFICENT BRO MY BRAIN AINT BRAINING SO I HARD CODED IT LMAO
        mb, ml, md, tub, tul, tud, wb, wl, wd, thb, thl, thd, fb, fl, fd, satb, satl, satd, sunb, sunl, sund = meal_plan_spilt(response) 

        return render_template("mealplan.html", MBREAK=mb, MLUNCH=ml, MDINNER=md,
        TUESBREAK=tub, TLUNCH=tul, TDINNER=tud,
        WEDBREAK=wb, WEDLUNCH=wl, WEDDINNER=wd,
        THUBREAK=thb, THULUNCH=thl, THUDINNER=thd,
        FRIBREAK=fb, FRILUNCH=fl, FRIDINNER=fd,
        SATBREAK=satb, SATLUNCH=satl, SATDINNER=satd,
        SUNBREAK=sunb, SUNLUNCH=sunl, SUNDINNER=sund
    )
        #RETURN CALL AI FUNCTION AND REUTRN OUTPUT AND GET

if __name__ == "__main__":
    #runs the app / website
    app.run(debug=True)

#http://127.0.0.1:5000
