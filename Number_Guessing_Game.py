"""
Guess-The-Number Game
"""
import random
import time

# Track high scores for each difficulty level
high_scores = {"Easy": None, "Medium": None, "Hard": None}

# Welcome message and game introduction
def play_game():
    welcome_message = """
    --------------------------------------------
    ::: Welcome to the Number Guessing Game! :::
    --------------------------------------------
    I am thinking of a number between 1 and 100.
    You will have a select number of chances depending on the difficulty.

    Please select the difficulty level:
    1. Easy (10 Chances)
    2. Medium (5 Chances)
    3. Hard (3 Chances)
    """
    print(welcome_message)

    # Determine user difficulty
    difficulty_levels = {"1": ("Easy", 10), "2": ("Medium", 5), "3": ("Hard", 3)}

    while True:
        game_choice = input("Enter your choice (1/2/3): ").strip()
        if game_choice in difficulty_levels:
            difficulty_name, attempts = difficulty_levels[game_choice]
            print(f"\nYou selected {difficulty_name} mode. You will have {attempts} attempts.")
            break
        else:
            print("Invalid choice. Please enter '1' for Easy, '2' for Medium, or '3' for Hard.")

    # Generate a random number between 1 and 100.
    secret_number = random.randint(1, 100)
    guess = None
    start_time = time.time() # Begin timer

    # Game loop.
    print(f"\nYou have {attempts} attempts to guess the correct number.")
    for attempt in range(1, attempts + 1):
        while True:
            try:
                guess = int(input(f"Attempt {attempt}/{attempts} - Enter your guess: "))
                break
            except ValueError:
                print(f"Invalid input! Please enter a valid integer.")

        # Review guess
        if guess < secret_number:
            print(f"Incorrect! The secret number is greater than {guess}.\n")
        elif guess > secret_number:
            print(f"Incorrect! The secret number is less than {guess}.\n")
        else:
            # User guessed correctly
            end_time = time.time() # End timer
            time_taken = round(end_time - start_time, 2)
            print(f"Congratulations! You guessed the number {secret_number} in {attempt} attempts!")
            print(f"Time Taken: {time_taken} seconds")

            # Update high score
            if high_scores[difficulty_name] is None or attempt < high_scores[difficulty_name]:
                high_scores[difficulty_name] = attempt
                print(f"New High Score for {difficulty_name}! Only {attempt} attempts!")
            else:
                print(f"Current High Score for {difficulty_name}: {high_scores[difficulty_name]} attempts")

            return high_scores # Exit loop and return new high score

        # Hint System - provide hint every 3 attempts
        if attempt % 3 == 0 and attempt != attempts:
            distance = abs(secret_number - guess)

            #Dynamically shrink hint range
            if distance > 50:
                hint_range = 15 # Wide range
            elif distance > 20:
                hint_range = 10 # Medium range
            else:
                hint_range = 5 # Narrow range

            lower_bound = max(1, secret_number - hint_range)
            upper_bound = min(100, secret_number + hint_range)
            print(f"Hint: The number is between {lower_bound} and {upper_bound}.")

    # Runs if user fails to guess secret number in attempts allotted
    print(f"Nope. The correct number was {secret_number}.")

    return high_scores # Return existing high score

# Main loop for playing multiple rounds
while True:
    play_game()

    # Ask if the user would like to play an additional round
    play_again = input("\nWould you like to play another game? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print(f"Thank you for playing. See you next time.")
        break
