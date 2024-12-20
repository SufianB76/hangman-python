import random

def hangman():
    words = ["python", "developer", "hangman", "terminal", "programming"]
    word_to_guess = random.choice(words).lower()
    word_length = len(word_to_guess)
    guessed_word = ["_" for _ in word_to_guess]
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print(f"The word has {word_length} letters.")

    while incorrect_guesses < max_incorrect_guesses:
        print("\nCurrent word: " + " ".join(guessed_word))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print("Good guess!")
            for index, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[index] = guess

            if "_" not in guessed_word:
                print("\nCongratulations! You've guessed the word:", word_to_guess)
                break
        else:
            print("Incorrect guess.")
            incorrect_guesses += 1

    if "_" in guessed_word:
        print(f"\nGame over! The word was: {word_to_guess}")

    play_again = input("Would you like to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    hangman()
