# Hangman Game

A simple console-based Hangman game written in Python. This game allows the player to guess letters in a randomly selected word until they either guess the word correctly or run out of attempts.

## Features

- **Random Word Selection**: A word is randomly chosen from a predefined list.
- **Letter Guessing**: Players guess letters to reveal the word.
- **Incorrect Guesses Tracking**: Tracks incorrect guesses and limits the number of allowed incorrect guesses.
- **Win/Loss Conditions**: The game ends when the player either correctly guesses the word or exhausts the allowed number of incorrect guesses.

## Installation

Ensure you have Python installed. This game does not require any additional libraries.

1. Clone the repository or download the code:
    ```bash
    git clone https://github.com/yourusername/hangman-game.git
    ```

2. Navigate to the project directory:
    ```bash
    cd hangman-game
    ```

## Running the Game

To start the game, run the following command in your terminal:

```bash
python hangman.py
```

## Gameplay

1. The game will display underscores representing the letters in the word.
2. Input a single letter to guess.
3. The game will update the display based on correct or incorrect guesses.
4. The game ends when you either guess all the letters in the word or run out of attempts.

## Example

```
Welcome to Hangman!
_ _ _ _ _ _
Guess a letter: a
Good guess!
_ _ a _ _ _
Guess a letter: e
Incorrect! You have 5 attempts left.
_ _ a _ _ _
Guess a letter: s
Good guess!
_ _ a s _ _
...
Congratulations, you won!
```

## Customization

- **Add More Words**: Update the `WORDS` list in the `hangman.py` file with additional words.
- **Improve UI**: Enhance the user interface or add graphical elements by integrating with libraries like Pygame.
- **Add Difficulty Levels**: Implement difficulty levels by categorizing words into easy, medium, and hard.

## Contributing

Feel free to fork the repository and submit pull requests with improvements or fixes. Please follow the coding style and guidelines provided in the code.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
