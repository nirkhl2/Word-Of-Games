import os

import MainScores
import Utils


def add_score(game_difficulty):
    try:
        points_of_winning = (game_difficulty * 3) + 5
        file = open(Utils.SCORES_FILE_NAME, "r")  # open file in write mode and create one if does not exist
        current_score = file.read()
        if current_score.isnumeric():
            updated_points_of_winning = int(current_score) + points_of_winning
            file = open(Utils.SCORES_FILE_NAME, "w")  # open file in write mode and create one if does not exist
            file.write(str(updated_points_of_winning))  # write to file
            print("current score is: '" + current_score + "', your updated score is: '" + str(updated_points_of_winning) + "'")
        else:
            print(str(Utils.SCORES_FILE_NAME) + " has data that is not numeric, exiting")
            exit(Utils.BAD_RETURN_CODE)

    except Exception as e:
        try:
            if os.path.exists(Utils.SCORES_FILE_NAME):
                os.remove(Utils.SCORES_FILE_NAME)
        except:
            pass
        file = open(Utils.SCORES_FILE_NAME, "w")  # open file in write mode and create one if does not exist
        file.write(str(points_of_winning))  # write to file

    finally:
        file.close()
        MainScores.app.run()
