import random

GAME_BOOL = True

def try_again():
    """A dummy docstring."""
    print("\nWould you like to play again? (Y/N)")

    try:
        response = str(input()).lower()
    
        if response == 'y' or 'yes':
            return True
        elif response == 'n' or 'no':
            return False
    except ValueError:
        print("\nPlease provide a valid response.")
        return try_again()

def game_explanation():
    """A dummy docstring."""
    print("\nI'm thinking of a number between 1 and 10.")
    print("\nYou only have one chance to guess right.")

def guess_number():
    """A dummy docstring."""
    try:
        user_guess = int(input())
        return user_guess
    except ValueError:
        print("\nPlease provide a valid integer.")
        return guess_number()

print('Welcome to the number guessing game!')

while GAME_BOOL is True:
    game_explanation()

    RandomInteger = random.randint(1, 10)

    Guess = guess_number()

    if Guess == RandomInteger:
        print("\nThat's right! You win!")
    else:
        print("\nSorry, that's wrong. The number was", RandomInteger)

    Retry = try_again()
    
    if Retry is False:
        print("\nThanks for playing!")
        GAME_BOOL = False
        break
