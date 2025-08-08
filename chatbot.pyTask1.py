he# chatbot.py

# A function is a block of organized, reusable code that is used to
# perform a single, related action. This function, `get_response`,
# handles the core logic of our chatbot.
def get_response(user_input):
    """
    Determines the chatbot's response based on the user's input using
    a series of if-elif-else conditional statements.

    Args:
        user_input (str): The text input from the user.

    Returns:
        str: The corresponding chatbot response.
    """
    # The .lower() method is used to convert the input to lowercase.
    # This makes the comparison case-insensitive, so "Hello", "hello",
    # and "HELLO" are all treated the same.
    normalized_input = user_input.lower()

    # The if-elif-else block is a control flow statement that allows
    # the program to make decisions. It checks each condition in order.
    # The first condition that evaluates to True will have its code executed.
    if normalized_input == "hello":
        return "Hi!"
    elif normalized_input == "how are you":
        return "I'm fine, thanks!"
    elif normalized_input == "bye":
        return "Goodbye!"
    else:
        # The 'else' block is a fallback. It runs only if none of the
        # preceding 'if' or 'elif' conditions are met.
        return "I'm sorry, I don't understand that."

# This is the main function that runs the chatbot.
# It uses a loop to keep the conversation going.
def run_chatbot():
    """
    Manages the conversation flow, including prompting the user,
    getting their input, and printing the chatbot's output.
    """
    print("Welcome to the simple rule-based chatbot!")
    print("You can say 'hello', 'how are you', or 'bye'.")
    print("---------------------------------------------")

    # A 'while True' loop creates an infinite loop. This keeps the
    # program running continuously until a 'break' statement is encountered.
    # This is how we keep the conversation going.
    while True:
        # INPUT: The 'input()' function pauses the program and prompts
        # the user for text. It returns the text as a string.
        user_input = input("You: ")
        
        # We call our `get_response` function, passing the user's input to it.
        # This is where our chatbot's logic is executed.
        response = get_response(user_input)
        
        # OUTPUT: The 'print()' function displays the response back to the user.
        print(f"Chatbot: {response}")

        # We check the normalized input again to decide if we should exit the loop.
        if user_input.lower() == "bye":
            # The 'break' statement immediately terminates the 'while' loop.
            # This is how the program ends gracefully.
            break

# The `if __name__ == "__main__"` block is a standard Python idiom.
# It ensures that the `run_chatbot()` function is only called when the
# script is executed directly, not when it is imported as a module into another script.
if __name__ == "__main__":
    run_chatbot()
