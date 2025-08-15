print("Chatbot: Hi! I’m your simple chatbot. Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hi":
        print("Chatbot: Hello! How are you?")
    elif user in ["good", "fine", "great"]:
        print("Chatbot: That’s nice to hear!")
    elif user == "what is your name":
        print("Chatbot: I’m PythonBot, your assistant.")
    elif user == "bye":
        print("Chatbot: Goodbye! Have a nice day!")
        break
    else:
        print("Chatbot: I don't understand that yet.")
