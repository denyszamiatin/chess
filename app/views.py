# coding: utf-8
from app import app
from flask import render_template
from chessboard import init_board, create_default_position

@app.route('/')
@app.route('/index')
def index():
    board = create_default_position(init_board())
    return render_template("index.html",board = board)
