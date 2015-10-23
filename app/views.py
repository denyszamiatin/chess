# coding: utf-8
from flask import render_template, Flask, request
from chessboard import init_board, create_default_position, is_pawn, convert_coords_to_indexes,try_move_a_pawn,\
    log_move, get_figure

app = Flask(__name__)
board = create_default_position(init_board())

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", board=board)

@app.route('/move')
def do_move():
    move = request.args.get('move')
    if is_pawn(board,convert_coords_to_indexes(move[:2])):
        try_move_a_pawn(board, move[:2], move[2:])
        index = convert_coords_to_indexes(move[2:])
        logs = log_move(move[:2],move[2:],get_figure(board,index[0],index[1]))
    return render_template("index.html", board=board,logs=logs)


app.run(debug=True)
