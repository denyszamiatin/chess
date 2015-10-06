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


def convert_coords_to_indexes(coordinate):
    """Converts chess coordinates to list indexes
    >>> convert_coords_to_indexes("e2")
    (6, 4)
    >>> convert_coords_to_indexes("h8")
    (0, 7)
    """
    return VERTICAL_NAMES.index(coordinate[1]), HORIZONTAL_NAMES.index(coordinate[0])
