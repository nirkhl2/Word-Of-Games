import GuessGame
import MemoryGame
import CurrencyRouletteGame

global user_name, game_name, game_difficulty
games_names_list = ['Memory Game', 'Guess Game', 'Currency Roulette']
user_input_type_list = ['game', 'difficulty']


def set_user_name(name):
    global user_name
    user_name = name


def welcome(name):
    set_user_name(name)
    return ("--- Hello " + str(name) + " and welcome to the World of Games (WoG). \n"
                                       "Here you can find many cool games to play\n\n")


def load_game():
    select_game()
    select_game_difficulty()
    if game_name == games_names_list[0]:
        MemoryGame.play(game_difficulty)
    elif game_name == games_names_list[1]:
        GuessGame.play(game_difficulty)
    elif game_name == games_names_list[2]:
        CurrencyRouletteGame.play(game_difficulty)


def select_game():
    user_input = input("--- Please choose a game to play: \n"
                       "1. " + games_names_list[0] + " - a sequence of numbers will appear for 1 second and you have to guess it back. \n"
                                                     "2. " + games_names_list[1] + " - guess a number and see if you chose like the computer. \n"
                                                                                   "3. " + games_names_list[2] + " - try and guess the value of a random amount of USD in ILS. \n\n")
    if verify_user_input(user_input, input_type='game'):
        global game_name
        game_name = str(games_names_list[int(user_input) - 1])


def select_game_difficulty():
    user_input = input("--- Please choose the difficulty level of gameplay for game '" + str(game_name) + "': \n"
                       "Possible options between 1 (Beginner level) to 5 (All-Star level).\n\n")
    if verify_user_input(user_input, input_type='difficulty'):
        global game_difficulty
        game_difficulty = int(user_input)


def verify_user_input(user_input, input_type):
    if input_type == str(user_input_type_list[0]):  # verify the input of 'game' field
        if user_input.isnumeric() and int(user_input) in range(1, 4):
            print("Hi '" + user_name + "'! you have selected game number '" + str(user_input) + "',game name: '" + str(games_names_list[int(user_input) - 1]) + "'. Good luck!")
            return True
        else:
            print("Invalid input for '" + str(input_type) + "', expected input values are between 1-3, while your input value is: '" + str(user_input) + "'.")
            print("Please try again...\n")
            select_game()
    elif input_type == str(user_input_type_list[1]):  # verify the input of 'difficulty' field
        if user_input.isnumeric() and int(user_input) in range(1, 6):
            print("Hi '" + user_name + "'! you have selected difficulty level '" + str(user_input) + "',game name: '" + str(game_name) + "'. Good luck!")
            return True
        else:
            print("Invalid input for '" + str(input_type) + "', expected input values are between 1-5, while your input value is: '" + str(user_input) + "'.")
            print("Please try again...\n")
            select_game_difficulty()
