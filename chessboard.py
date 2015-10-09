BOARD_SIZE = 8
EMPTY_CELL = '.'
VERTICAL_NAMES = '87654321'
HORIZONTAL_NAMES = 'abcdefgh'


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
    return HORIZONTAL_NAMES[column] + VERTICAL_NAMES[row]


def convert_coords_to_indexes(coordinate):
    """Converts chess coordinates to list indexes
    >>> convert_coords_to_indexes("e2")
    [6, 4]
    >>> convert_coords_to_indexes("h8")
    [0, 7]
    """
    try:
        return [
            VERTICAL_NAMES.index(coordinate[1]),
            HORIZONTAL_NAMES.index(coordinate[0])
        ]
    except (ValueError, IndexError):
        raise ValueError("Invalid coords")


def create_default_position(board):
    """
    Set up chess board
    White is uppercase
    p - pawns
    r - rook
    k - knight
    b - bishop
    q - queen
    m - king
    """
    board[0] = ['r', 'k', 'b', 'q', 'm', 'b', 'k', 'r']
    board[1] = ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p']
    board[6] = ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']
    board[7] = ['R', 'K', 'B', 'Q', 'M', 'B', 'K', 'R']

    return board


def get_figure(board, row, column):
    return board[row][column]


def print_board(board):
    """
    Print chessboard
    """
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            print get_figure(board, i, j),
        print


def check_pawn_move(board, start, dest):
    """
    Cheking - is move availible for pawn
    returns True or False
    >>> board = create_default_position(init_board())
    >>> check_pawn_move(board, [6,4],[5,4])
    True
    >>> check_pawn_move(board, [6,4],[1,4])
    False
    """
    return get_figure(board, start[0], start[1]) in "Pp" and \
           get_figure(board, dest[0], dest[1]) == EMPTY_CELL and \
           start[1] == dest[1] and \
           abs(start[0] - dest[0]) == 1


def check_horizontal(board, coords):
    """
    Get horizontal figure
    >>> board = create_default_position(init_board())
    >>> check_horizontal(board, 'a1')
    ['R', 'K', 'B', 'Q', 'M', 'B', 'K', 'R']
    >>> check_horizontal(board, 'a2')
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']
    >>> check_horizontal(board, 'a6')
    ['.', '.', '.', '.', '.', '.', '.', '.']
    """
    return board[convert_coords_to_indexes(coords)[0]]

if __name__ == '__main__':
    board = create_default_position(init_board())
    while True:
        print_board(board)
        action = raw_input("?")
        if action in 'Qq':
            break
        try:
            indexes = convert_coords_to_indexes(action)
        except ValueError as e:
            print e
            continue
        print get_figure(board, indexes[0], indexes[1])
