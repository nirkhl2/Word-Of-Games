import random
import Live

global secret_number, user_guess


def welcome_to_the_game():
    print("\n\n")
    print('------------------------------------------------------------------------\n' * 3 + '------------------------------------------------------------------------')
    print("++++++ Welcome to game '" + str(Live.game_name) + "'! difficulty level: '" + str(Live.game_difficulty) + "' ++++++")
    print('------------------------------------------------------------------------\n' * 4)


def generate_number(game_difficulty):
    global secret_number
    secret_number = random.randint(1, int(game_difficulty))


def get_guess_from_user(game_difficulty):
    user_input = input("Please guess the secret number value (between 1 to " + str(game_difficulty) + ")\n")
    if verify_user_input(user_input, game_difficulty):
        global user_guess
        user_guess = int(user_input)


def verify_user_input(user_input, game_difficulty):
    if user_input.isnumeric() and int(user_input) in range(1, int(game_difficulty) + 1):
        print("Hi " + Live.user_name + "! you have selected number '" + str(user_input) + "', as a guess for '" + str(Live.game_name) + "'. Good luck!")
        return True
    else:
        print("Invalid input for guess, expected input values are between 1-" + str(game_difficulty) + ", while your input value is: '" + str(user_input) + "'.")
        print("Please try again...\n")
        get_guess_from_user(game_difficulty)


def compare_results(guess_value, secret_number_value):
    if guess_value != secret_number_value:
        return False
    else:
        return True


def user_won():
    print("\n--- Hi " + Live.user_name + "! You WON the game '" + str(Live.game_name) + "'! :)\n Your guess is '"
          + str(user_guess) + "', same as the secret number value: '" + str(secret_number) + "'. ---")


def user_lost():
    print("\n--- Hi " + Live.user_name + "! You LOST the game '" + str(Live.game_name) + "'! :(\n Your guess is '"
          + str(user_guess) + "', while secret number value is  '" + str(secret_number) + "'. ---")


def play(game_difficulty):
    welcome_to_the_game()
    generate_number(game_difficulty)  # generate secret number
    get_guess_from_user(game_difficulty)  # get input from user
    is_user_winner = compare_results(user_guess, secret_number)
    if is_user_winner:
        user_won()
        return True
    else:
        user_lost()
        return False
