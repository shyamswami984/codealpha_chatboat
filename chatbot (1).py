# ============================================
# TASK 4: Rule-Based Chatbot
# Concepts: if-elif, functions, loops, I/O
# ============================================

def get_response(user_input):
    """
    Takes user input and returns a predefined reply.
    Uses if-elif-else to match patterns.
    """
    # Normalize input: lowercase and strip spaces
    message = user_input.lower().strip()

    # ---------- Greetings ----------
    if message in ["hello", "hi", "hey"]:
        return "Hi there! 😊 Nice to meet you!"

    # ---------- How are you ----------
    elif message in ["how are you", "how r u", "how are you doing"]:
        return "I'm doing great, thanks for asking! How about you?"

    # ---------- Bot's name ----------
    elif message in ["what is your name", "your name", "who are you"]:
        return "I'm SimpleBot — a rule-based chatbot! 🤖"

    # ---------- Help / Capabilities ----------
    elif message in ["help", "what can you do"]:
        return ("I can respond to:\n"
                "  • hello / hi / hey\n"
                "  • how are you\n"
                "  • what is your name\n"
                "  • tell me a joke\n"
                "  • good morning / good night\n"
                "  • bye / goodbye")

    # ---------- Joke ----------
    elif message in ["tell me a joke", "joke"]:
        return "Why do programmers prefer dark mode?\nBecause light attracts bugs! 🐛😄"

    # ---------- Gratitude ----------
    elif "thank" in message:
        return "You're welcome! 😊 Happy to help."

    # ---------- Time-based greetings ----------
    elif "good morning" in message:
        return "Good morning! ☀️ Hope you have a wonderful day!"

    elif "good night" in message:
        return "Good night! 🌙 Sweet dreams!"

    # ---------- Exit ----------
    elif message in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! 👋 It was nice chatting with you!"

    # ---------- Default / Unknown ----------
    else:
        return ("I didn't understand that. 🤔\n"
                "Type 'help' to see what I can do.")


def chat():
    """
    Main function: runs the chatbot in a loop.
    Uses a while loop to keep the conversation going.
    Exits when user types 'bye', 'exit', or 'quit'.
    """
    print("=" * 40)
    print("       Welcome to SimpleBot! 🤖")
    print("  Type 'bye' or 'exit' to quit.")
    print("=" * 40)
    print()

    # ----- LOOP: keeps chatbot running -----
    while True:
        # ----- INPUT: get message from user -----
        user_input = input("You: ")

        # Skip empty input
        if not user_input.strip():
            continue

        # ----- OUTPUT: print bot's response -----
        response = get_response(user_input)
        print(f"Bot: {response}")
        print()

        # Exit condition
        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            break


# ---- Entry point ----
if __name__ == "__main__":
    chat()
