

def create_default_ches_position(board):
    board[7] = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
    board[0] = ['ROOK', 'KINGHT', 'BISHOP', 'QUEEN', 'KING', 'BISHOP', 'KNIGHT', 'ROOK']
    board[6] = ['pawns', 'pawns', 'pawns', 'pawns', 'pawns', 'pawns', 'pawns', 'pawns']
    board[1] = ['PAWNS', 'PAWNS', 'PAWNS', 'PAWNS', 'PAWNS', 'PAWNS', 'PAWNS', 'PAWNS']
    return board
