# coding: utf-8
from app import app
from flask import render_template
from chessboard import init_board
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
