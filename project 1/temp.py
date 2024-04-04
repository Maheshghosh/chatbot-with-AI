def chatbot_response(user_input):
    # Convert user input to lowercase for case insensitivity -----

    user_input = user_input.lower()

    # some rules for the chatbot -------

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "whats your name" in user_input:
        return "My name is SHIFRA"
    elif "how are you" in user_input:
        return "I'm doing fine! How are you?"
    elif "i am also fine" in user_input:
        return "okey!good"
    elif "i want to ask question" in user_input:
        return "what?"
    elif "i am craving some italian food" in user_input:
        return"Great choice! There's a nice Italian restaurant called Mamma Mia's just a few blocks away. Would you like more information about it?"
    elif "Yes, please Can you tell me about their menu" in user_input:
        return" I'm sorry, I don't have access to their menu information. But you can check their website or give them a call for more details"
    elif "What's your favorite color" in user_input:
        return"I'm sorry, I didn't understand that. Can you please rephrase or ask something else?"
    elif "Alright, let's try something else. Can you tell me a joke" in user_input:
        return"I'm sorry, I didn't understand that. Can you please rephrase or ask something else?"
    elif "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "weather" in user_input:
        return "I'm sorry, I am not equipped to provide weather information."
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask something else?"
    


     # Test the chatbot -------

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
