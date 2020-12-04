import random
import time
import Live
lst_random_nums = []
lst_user_guess_nums = []


def welcome_to_the_game():
    print("\n\n")
    print('------------------------------------------------------------------------\n' * 3 + '------------------------------------------------------------------------')
    print("+++++++++ Welcome to game '" + str(Live.game_name) + "'! difficulty level: '" + str(Live.game_difficulty) + "' +++++++++")
    print('------------------------------------------------------------------------\n' * 4)


def generate_sequence(game_difficulty):
    global lst_random_nums
    lst_random_nums = []
    for i in range(0, int(game_difficulty)):
        num = random.randint(1, 101)
        lst_random_nums.append(num)
    # print(lst_random_nums)


def print_rand_list_to_screen_for_1_sec():
    for i in [5, 4, 3, 2, 1]:
        print(f'\r-------- +++++++ Be ready, the list to memorize will appear in {i}... +++++++ --------', end='', flush=True)
        time.sleep(1)

    for i in [lst_random_nums, '']:
        print(f'\r{str(i)}', end='', flush=True)
        time.sleep(3)


def get_list_from_user(game_difficulty):
    print("\n--- +++ Please select user input as list the list you have memorized")
    for i in range(game_difficulty):
        get_guess_from_user_index(int(i))


def get_guess_from_user_index(list_index):
    user_input = input("please select the input for you guess list, this is your input for list index " + str(list_index+1) + ": ")
    if verify_user_input(user_input, list_index):
        # global lst_user_guess_nums
        lst_user_guess_nums.append(int(user_input))
    else:
        get_guess_from_user_index(list_index)


def verify_user_input(user_input, list_index):
    if user_input.isnumeric() and int(user_input) in range(1, 101):
        print(Live.user_name + ", you have selected number '" + str(user_input) + "', as a guess for list index: '" + str(list_index+1) + "'. Good luck!")
        return True
    else:
        print("Invalid input guess list index '" + str(list_index) + "' expected input values are between 1 to 101, while your input value is: '" + str(user_input) + "'.")
        print("Please try again...\n")
        get_list_from_user(list_index)


def user_won():
    print("\n--- Hi " + Live.user_name + "! You WON the game '" + str(Live.game_name) + "'! :)\n Your guess is '"
          + str(lst_user_guess_nums) + "', as the random list value is '" + str(lst_random_nums) + "'. ---")


def user_lost():
    print("\n--- Hi " + Live.user_name + "! You LOST the game '" + str(Live.game_name) + "'! :(\n Your guess is '"
          + str(lst_user_guess_nums) + "', while the shuffled list values are '" + str(lst_random_nums) + "'. ---")


def is_list_equal():
    if lst_random_nums == lst_user_guess_nums:
        return True
    else:
        return False


def play(game_difficulty):
    welcome_to_the_game()
    generate_sequence(game_difficulty)
    print_rand_list_to_screen_for_1_sec()
    get_list_from_user(game_difficulty)  # get input from user
    if is_list_equal():
        user_won()
        return True
    else:
        user_lost()
        return False
