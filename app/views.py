# coding: utf-8
from flask import render_template, Flask, request
from chessboard import init_board, create_default_position

app = Flask(__name__)
board = create_default_position(init_board())

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", board=board)

@app.route('/move')
def do_move():
    print request.args.get('move')
    return render_template("index.html", board=board)


app.run(debug=True)