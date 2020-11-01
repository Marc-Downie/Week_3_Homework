from flask import render_template, request
from app import app
from app.models.player_choice import players
from app.models.player import *
from app.models.game import *

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/game', methods=['POST'])
def game():
    player1 = Player("Marc", None)
    player2 = Player("Linzi", None) 
    player1.selection = request.form["player1"].title().strip()
    player2.selection = request.form["player2"].title().strip()
    game = Game(player1, player2)
    result = game.play_game()

    return render_template('game.html', title='Home', results=result)


    