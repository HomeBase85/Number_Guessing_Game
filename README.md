# Guess-the-Number Game

Welcome to the **Guess-the-Number Game**, an interactive number guessing game where you challenge your logic and intuition to guess a randomly generated number! With multiple difficulty levels, this game is fun for all skill levels. Can you beat the high score?

---

## Features
- Three difficulty levels: 
  - **Easy**: 10 attempts
  - **Medium**: 5 attempts
  - **Hard**: 3 attempts
- Real-time hints after every 3 incorrect guesses
- High score tracking for each difficulty level
- Dynamic feedback to guide your guesses
- Play multiple rounds in a single session

---

## How to Play

1. Run the script in a Python interpreter:
   ```bash
   python Number_Guessing_Game.py
   ```

2. Select a difficulty level by entering one of the following options:
   - `1` for Easy
   - `2` for Medium
   - `3` for Hard

3. Guess the number within the allotted attempts.
   - You will receive feedback whether your guess is too high or too low.

4. If you guess incorrectly for 3 attempts, you'll receive a hint narrowing the range.

5. Try to guess the number in the fewest attempts possible to beat the high score!

6. After the game ends, you can choose to play another round or exit.

---

## Game Logic Overview

1. **Random Number Generation:** A number between 1 and 100 is randomly chosen for each game.

2. **Difficulty Levels:** The number of allowed attempts is determined by the difficulty level:
   - Easy: 10 attempts
   - Medium: 5 attempts
   - Hard: 3 attempts

3. **Hint System:** If the guess is incorrect and the attempt count is a multiple of 3, a range-based hint is provided:
   - Wide range (15 numbers) for guesses far from the secret number.
   - Medium range (10 numbers) for closer guesses.
   - Narrow range (5 numbers) for guesses very near the secret number.

4. **High Score Tracking:** The game keeps track of the best scores for each difficulty level.

---

## Requirements

- Python 3.7 or higher
- No additional libraries are required as the game relies on the standard Python library.

---

## Example Gameplay

```
--------------------------------------------
::: Welcome to the Number Guessing Game! :::
--------------------------------------------
I am thinking of a number between 1 and 100.
You will have a select number of chances depending on the difficulty

Please select the difficulty level:
1. Easy (10 Chances)
2. Medium (5 Chances)
3. Hard (3 Chances)

Enter your choice (1/2/3): 2

You selected Medium mode. You will have 5 attempts.

You have 5 attempts to guess the correct number.
Attempt 1/5 - Enter your guess: 50
Incorrect! The secret number is greater than 50.

Attempt 2/5 - Enter your guess: 75
Incorrect! The secret number is less than 75.

Attempt 3/5 - Enter your guess: 60
Hint: The number is between 55 and 65.
...
```

---

## Author

This project was created as a fun programming exercise to practice Python fundamentals and game logic development. Feel free to contribute, provide feedback, or use the code for your own projects!

---

## License

This project is open-source and free to use under the MIT License. Contributions and improvements are welcome!
