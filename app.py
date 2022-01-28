from flask import Flask, request, render_template, jsonify
from uuid import uuid4

from boggle import BoggleGame

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

# The boggle games created, keyed by game id
games = {}


@app.get("/")
def homepage():
    """Show board."""

    return render_template("index.html")


@app.post("/api/new-game")
def new_game():
    """Start a new game and return JSON: {game_id, board}.
    >>> new_game()
    >>> json_as_text = json_response.get_data(as_text=True)
    >>> len(json_as_text.board) == 5
    True
    >>> len(json_as_text.board[0]) == 5
    True
    >>> type(json_as_text.gameId) == 'str'
    True

    """

    # get a unique string id for the board we're creating
    game_id = str(uuid4())
    game = BoggleGame()
    games[game_id] = game

    json_response = jsonify({
        "gameId": game_id,
        "board": game.board
    })

    print(f"{json_response.get_data(as_text=True)}")

    return json_response
