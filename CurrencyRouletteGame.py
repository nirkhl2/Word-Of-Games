import random
import sys
import requests
import Live
global random_number, user_guess, money_interval


def welcome_to_the_game():
    print("\n\n")
    print('------------------------------------------------------------------------\n' * 3 + '------------------------------------------------------------------------')
    print("++++++ Welcome to game '" + str(Live.game_name) + "'! difficulty level: '" + str(Live.game_difficulty) + "' ++++++")
    print('------------------------------------------------------------------------\n' * 4)


def get_guess_from_user():
    user_input = input("Please guess the currency between USD and ILS to number '" + str(random_number) + "': \n")
    if verify_user_input(user_input):
        global user_guess
        user_guess = int(user_input)


def verify_user_input(user_input):
    if user_input.isnumeric():
        print("Hi " + Live.user_name + "! you have selected number '" + str(user_input) + "', as a guess for '" + str(Live.game_name) + "'. Good luck!")
        return True
    else:
        print("Invalid input for guess, as it's not numeric. your input value is: '" + str(user_input) + "', while expected numeric value")
        print("Please try again...\n")
        get_guess_from_user()


def generate_random_number():
    global random_number
    random_number = random.randint(1, 101)


def get_money_interval(game_difficulty):
    money_interval_aka_t = int(get_api_response_for_currency() * random_number)  # (currency between USD to ILS)*(random between 1 to 100)
    difficulty_interval_aka_d = int(game_difficulty)

    # (t - (5 - d))
    low_interval_value = money_interval_aka_t - (5-difficulty_interval_aka_d)
    # (t + (5 - d))
    max_interval_value = money_interval_aka_t + (5-difficulty_interval_aka_d)
    global money_interval
    money_interval = [low_interval_value, max_interval_value]


# API: https://currencydatafeed.com/panel/api
# User & Pass: Gmail + regular password
# Limitation: can be used up to 500 times with single token (but a token can be reset)
def get_api_response_for_currency():
    url = "https://currencydatafeed.com/api/data.php?token=vyg1c44wty013pm7f6ot&currency=USD/ILS"
    try:
        resp = requests.get(url, timeout=3)
        return float(resp.json()["currency"][0]["value"])  # Parse the json response to get the relevant value
    except requests.exceptions.HTTPError as errh:
        print("Http Error while getting ILS currency from api, exception: ", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting while getting ILS currency from api, exception: ", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error while getting ILS currency from api, exception: ", errt)
    except requests.exceptions.RequestException as err:
        print("Exception occurred while getting ILS currency from api, exception: ", err)
    sys.exit(1)


def is_guess_in_range(allowed_interval):
    return user_guess in range(allowed_interval[0], allowed_interval[1])


def user_won():
    print("\n--- Hi " + Live.user_name + "! You WON the game '" + str(Live.game_name) + "'!!\n your guess is '"
          + str(user_guess) + "', as the currency allowed range is: '" + str(('-'.join(str(x) for x in money_interval)) + "'. ---"))


def user_lost():
    print("\n--- Hi " + Live.user_name + "! You LOST the game '" + str(Live.game_name) + "'!!\n your guess is '"
          + str(user_guess) + "', while the currency allowed range is: '" + str(('-'.join(str(x) for x in money_interval)) + "'. ---"))


def play(game_difficulty):
    welcome_to_the_game()
    generate_random_number()
    get_money_interval(game_difficulty)
    get_guess_from_user()
    if is_guess_in_range(money_interval):
        user_won()
        return True
    else:
        user_lost()
        return False
