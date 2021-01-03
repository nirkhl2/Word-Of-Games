import platform
import os
global SCORES_FILE_NAME, BAD_RETURN_CODE
SCORES_FILE_NAME = "scores.txt"
BAD_RETURN_CODE = 1


def screen_cleaner():
    if platform.system().__eq__("Windows"):
        os.system('cls')  # Windows
    else:
        os.system('clear')  # linux
