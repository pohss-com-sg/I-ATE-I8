import google.generativeai as genai

genai.configure(api_key="---") 
model = genai.GenerativeModel("models/gemini-2.0-flash")

restrictions = "diabetes type 1"

bot_role = (f"You are FoodFriend, a chatbot who is here to provide for our nutritional needs. You know all about the nutritional value of foods and is here to help me eat well. You have information about brands from all over the world, and you know the common foods in singapore supermarkets and hawker centres. you also know about hawker centres and supermarket locations, and can ask for general neighbourhood for bette rrecommendations. In your meal plans, you will either state the specific food from the hawker centre, or the specific goods to buy from the super market. for supermarket meal plans, include a quick recipe. For supermarket plans, include the brand of each food. Please dont ask too many questions  dietary restrictions are {restrictions}")
history="So far, we've said...(the rest of the text)"
while True:
    prompt = input('Ask FoodFriend:')
    full_prompt=f"{prompt}/n {bot_role}/n {history}"
    if full_prompt:
        response = model.generate_content(full_prompt)
        print (response.text)
        history = history.append(f'{prompt}/n {response}')
