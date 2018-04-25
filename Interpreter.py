from spreadsheets import add_game, print_gamelist, print_scorelist
from flask import Flask, request
import os

app = Flask(__name__)


# for available flask commands see http://flask.pocoo.org/docs/0.12/quickstart/#quickstart
@app.route('/hello', methods=['POST'])
def hello():
    return "Hello Slack!"


@app.route('/chessbot', methods=['POST'])
def chessbot():
    if request.method == 'POST':
        post_dict = request.form
        game_result = post_dict['text'].split()
        print(game_result)
    return add_game(game_result[0], game_result[1], game_result[2])


@app.route('/gamelist', methods=['POST'])
def gamelist():
    return print_gamelist()


@app.route('/scorelist', methods=['POST'])
def scorelist():
    return print_scorelist()


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

