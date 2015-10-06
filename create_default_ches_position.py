__author__ = 'rosto'

BOARD_SIZE = 8
EMPTY_CELL = 0

board = [[EMPTY_CELL for x in xrange(BOARD_SIZE)] for y in xrange(BOARD_SIZE)]


def create_default_ches_position(board):
    """

    :type board: object
    """
    board[7] = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
    board[0] = ['ROOK', 'KINGHT', 'BISHOP', 'QUEEN', 'KING', 'BISHOP', 'KNIGHT', 'ROOK']
    board[6] = ['pawns', 'pawns', 'pawns', 'pawns', 'pawns', 'pawns', 'pawns', 'pawns']
    board[1] = ['PAWNS', 'PAWNS', 'PAWNS', 'PAWNS', 'PAWNS', 'PAWNS', 'PAWNS', 'PAWNS']
    return board
