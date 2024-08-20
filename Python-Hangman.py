import random

# List of words to guess
WORDS = ['python', 'hangman', 'programming', 'challenge', 'developer']

def get_word():
    """
    Randomly selects a word from the list of words.
    """
    return random.choice(WORDS)

def display_word(word, guesses):
    """
    Displays the word with guessed letters and underscores for unknown letters.

    Args:
    word (str): The word to be guessed.
    guesses (set): The set of guessed letters.

    Returns:
    str: The word with guessed letters and underscores.
    """
    return ' '.join([letter if letter in guesses else '_' for letter in word])

def hangman():
    """
    Runs the Hangman game.
    """
    word = get_word()
    guesses = set()
    incorrect_guesses = set()
    max_attempts = 6
    attempts = 0

    print("Welcome to Hangman!")
    print(display_word(word, guesses))

    while attempts < max_attempts:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guesses or guess in incorrect_guesses:
            print("You've already guessed that letter.")
            continue

        if guess in word:
            guesses.add(guess)
            print("Good guess!")
        else:
            incorrect_guesses.add(guess)
            attempts += 1
            print(f"Incorrect! You have {max_attempts - attempts} attempts left.")

        current_display = display_word(word, guesses)
        print(current_display)

        if '_' not in current_display:
            print("Congratulations, you won!")
            break
    else:
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()
