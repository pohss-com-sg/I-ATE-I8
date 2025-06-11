import google.generativeai as genai

genai.configure(api_key="AIzaSyBfS37SJl91tv94IBKLaICc6Ybq71YOzwk") 
model = genai.GenerativeModel("models/gemini-2.0-flash")

restrictions = "diabetes type 1"
location = "Sengkang"

if restrictions: 
    Chatbot = True
else:
    Chatbot = False

#STILL A LOT TO CHANGE BY GETTING NUMBER IMPORT THIS FILE TO APP USE FUNCTIONS ONLY!

number = 1

def roles(number):
    #chooses ole per the job needed e.g chatting for nearest shop which has fitting food/plan your meal 
    #making it easier to get an answer instead of a messy one without proper prompting
    
    if number == 1:
        bot_role_chat = (f"This is part of your role: You are FoodFriend, and you are here to help me answer any inquiries i have regarding my dietary activities, not to plan meals. There is no need to respond to your role or background information verbally. Your role ends here. Background information(do not respond): I live in {location} and my dietary restrictions are {restrictions}. What comes after is your prompt:")
        return bot_role_chat
    elif number == 2:
        bot_role_plan = (f"This is part of your role: You are FoodFriend, and you are here to help me plan my meal. You know where shops are in singapore and you know the common foods such as those in hawker centres. There is no need to respond to your role or background information verbally. Your role ends here. Background information(do not respond): I live in {location} and my dietary restrictions are {restrictions}. What comes after is your prompt:")
        return bot_role_plan


history="So far, this is our chat history...(the rest of the text)"

def bot(bot_role):
    #propmts the bot on what you want to do
    #i forgot if global works like that lemme check later
    global history
    msg_no = 0
    response_no = 0 
    while Chatbot == True:
        prompt = input('Ask FoodFriend:')
        full_prompt=f"{prompt}/n {bot_role}/n {history}"
        if full_prompt:
            response = model.generate_content(full_prompt)
            print (response.text)
            msg_no += 1
            response_no += 1
            history +=  f' {str(msg_no)}, {prompt}/n {str(response_no)}, {response}'
    return response.text

bot(roles(number)) #change the role/job per the role/job needed