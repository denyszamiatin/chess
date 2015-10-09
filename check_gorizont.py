
from chessboard import *


def check_gorizontal(coords):
    """
    Get horizontal figure
    >>> check_gorizontal('a1')
    ['R', 'K', 'B', 'Q', 'M', 'B', 'K', 'R']
    >>> check_gorizontal('a2')
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']
    >>> check_gorizontal('a6')
    [0, 0, 0, 0, 0, 0, 0, 0]
    """
#   this is create test board
    board = create_default_position(init_board())
    return board[convert_coords_to_indexes(coords)[0]]
