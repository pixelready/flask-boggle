from flask import Flask, request, render_template, jsonify
from uuid import uuid4

from boggle import BoggleGame
from wordlist import WordList, english_words

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
    """

    # get a unique string id for the board we're creating
    game_id = str(uuid4())
    game = BoggleGame()
    games[game_id] = game

    json_response = jsonify({
        "gameId": game_id,
        "board": game.board
    })

    return json_response


@app.post("api/score-word")
def score_word():
    response = request.json
    game_id = response.get("gameId")
    word = response.get("word")
    game = games.get(game_id, "Game not found")
    
    
    # if not a word
    # return {result: "not-word"}

    if game.is_word_in_word_list(word) == False:
        return jsonify({"result": "not-word"})

    # if not on board
    # return {result: "not-on-board"}

    elif game.check_word_on_board(word) == False:
        return jsonify({"result": "not-on-board"})

    # if valid word 
    # return {result: "ok"}
    else:
        score = games.play_and_score_word(word)
        return jsonify({"result": "ok"})

    



