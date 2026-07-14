print("=" * 50)
print("🤖 Welcome to Rule-Based AI Chatbot")
print("=" * 50)
print("Type 'bye' to exit the chatbot.\n")

while True:
    user = input("You: ").lower().strip()

    if user == "hi" or user == "hello" or user == "hey":
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I am fine. Thank you for asking!")

    elif user == "what is your name":
        print("Bot: My name is RuleBot.")

    elif user == "who made you":
        print("Bot: I was created by Shivam using Python.")

    elif user == "what can you do":
        print("Bot: I can answer simple predefined questions.")

    elif user == "help":
        print("Bot: You can ask me greetings, my name, who made me, thank you, date, time and more.")

    elif user == "thank you" or user == "thanks":
        print("Bot: You're welcome!")

    elif user == "good morning":
        print("Bot: Good Morning! Have a wonderful day.")

    elif user == "good afternoon":
        print("Bot: Good Afternoon!")

    elif user == "good evening":
        print("Bot: Good Evening!")

    elif user == "bye" or user == "exit" or user == "quit":
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry! I don't understand that question.")