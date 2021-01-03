import os
import Utils
import signal
from flask import Flask
app = Flask(__name__)
score_html = "<html><head><title>Scores Game</title></head><body><h1>The score is <div id='score'>{SCORE}</div></h1><div>TO EXIT THIS PAGE NAVIGATE TO " \
             "http://127.0.0.1:5000/stopServer</div></body></html>"
error_html = "<html><head><title>Scores Game</title></head><body><body><h1><div id='score' style='color:red'>{ERROR}</div></h1></body></html>"


def score_server():
    try:
        file = open(Utils.SCORES_FILE_NAME, "r")  # open file in write mode and create one if does not exist
        current_score = file.read()
        return score_html.replace("{SCORE}", str(current_score))
    except Exception as e:
        return error_html.replace("{ERROR}", str(e))


@app.route("/")
def score_to_web_service():
    return score_server()


@app.route('/stopServer', methods=['GET'])
def stop_server():
    print("Server is shutting down...")
    os.kill(os.getpid(), signal.SIGINT)
