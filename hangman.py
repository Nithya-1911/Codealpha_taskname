import random

def play_hangman():
    """
    This function runs a simple text-based Hangman game.
    """
    words = ["python", "hangman", "keyboard", "program", "developer"]
    chosen_word = random.choice(words)
    word_display = ["_"] * len(chosen_word)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("I've chosen a word. You have 6 incorrect guesses to find it.")

    while incorrect_guesses < max_incorrect_guesses and "_" in word_display:
        print("\n" + " ".join(word_display))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
            continue

        guessed_letters.append(guess)
        
        if guess in chosen_word:
            print(f"Good guess! The letter '{guess}' is in the word.")
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    word_display[i] = guess
        else:
            incorrect_guesses += 1
            print(f"Sorry, the letter '{guess}' is not in the word.")

    # Game end
    print("\n" + " ".join(word_display))
    if "_" not in word_display:
        print("Congratulations! You won! The word was:", chosen_word)
    else:
        print("Game over! You ran out of guesses.")
        print("The word was:", chosen_word)

if __name__ == "__main__":
    play_hangman()