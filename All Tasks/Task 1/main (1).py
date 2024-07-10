def chat_bot(user_input):
    user_input=user_input.lower()
    
    if "hi" in user_input or"hello" in user_input or"hey" in user_input:
        return "Hi! I'm a chatbot build to answer your questions.How can I assist you today?"
    elif"how are you" in user_input:
        return "I'm good.What about you? "
    elif"what is your name" in user_input:
        return "My name is Buddy."
    elif "do you sleep" in user_input:
        return "Well, I never sleep and do not have baggy eyes."
    elif"are you human" in  user_input:
        return "No, I'm a robot who lives on electricity."
    elif "tell me an interesting fact" in user_input:
        return "Even though dragonflies have six legs, they cannot walk."
    elif"tell me a joke" in user_input:
        return "Why are snails slow? Because they’re carrying a house on their back."
    else:
        return "I'm sorry, I didn't understand that. Please rephrase your sentence."
        
        
print("Chatbot: Namaste! I'm a chatbot, I'm here to assist you!(type thank you to exit)")

while True:
    user_input = input("Me: ")  
    if user_input.lower() == 'thank you':
        print("Chatbot: Goodbye! Have a great day!")
        break  
    
    response = chat_bot (user_input)  
    print("Chatbot:", response) 