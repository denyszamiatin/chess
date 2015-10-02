__author__ = 'BohdanPidopryhora'

BOARD_SIZE = 8
EMPTY_CELL = 0


def init_board():
    """
    Initiates chess board
    """
    return [[EMPTY_CELL for x in xrange(BOARD_SIZE)] for y in xrange(BOARD_SIZE)]


def convert_indexes_to_coords(row, column):
    """this function convert index -1
    >>> convert_indexes_to_coords(7, 0)
    'a1'
    >>> convert_indexes_to_coords(0, 7)
    'h8'
    """
    VERTICAL_NAMES = '87654321'
    HORIZONTAL_NAMES = 'abcdefgh'
    return HORIZONTAL_NAMES[column] + VERTICAL_NAMES[row]

