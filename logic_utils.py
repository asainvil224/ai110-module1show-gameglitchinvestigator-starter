def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100
#FIX: Added the get_range_for_difficulty function to logic_utils.py, which is responsible for returning the appropriate range of numbers based on the selected difficulty level. This function allows the game to adjust the secret number's range according to the player's choice of difficulty, making the game more challenging or easier as needed. The function takes a string input representing the difficulty and returns a tuple with the low and high values for that difficulty level.

def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None
#FIX: Added the parse_guess function to logic_utils.py, which is responsible for taking the raw input from the user and attempting to convert it into an integer guess. This function handles various edge cases, such as empty input, non-numeric input, and even decimal numbers by converting them to integers. It returns a tuple indicating whether the parsing was successful, the parsed integer guess (or None if parsing failed), and an error message if applicable. This function is essential for validating user input before processing it in the game logic.

def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"
#FIX: Added the check_guess function to logic_utils.py, which is responsible for comparing the player's guess to the secret number and returning both the outcome (whether the guess is correct, too high, or too low) and a corresponding message that can be displayed to the player as feedback. This function is essential for the game logic to determine how to respond to the player's input and provide hints accordingly.

def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
#FIX: Added the update_score function to logic_utils.py, which calculates the player's score based on the outcome of their guess and the number of attempts they have made. The scoring system rewards players for winning quickly and penalizes them for incorrect guesses, with different point adjustments based on whether the guess was too high or too low. This function is crucial for maintaining the player's score throughout the game and providing an incentive to guess correctly in fewer attempts.