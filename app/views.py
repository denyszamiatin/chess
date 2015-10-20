# coding: utf-8
from flask import render_template, Flask
from chessboard import init_board, create_default_position

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    board = create_default_position(init_board())
    return render_template("index.html", board=board)

app.run(debug=True)