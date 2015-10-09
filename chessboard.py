BOARD_SIZE = 8
EMPTY_CELL = 0
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


def print_board():
    """
    Print chessboard
    """
    figure_list = []
    board = create_default_position(init_board())
    for i in VERTICAL_NAMES:
        for j in VERTICAL_NAMES:
            figure = get_figure(board, int(i) - 1, int(j) - 1)
            figure_list.append(figure)
    for item in range(0, 64):
        if item % 8 == 0:
            print figure_list[item: item + 8]


def check_pawn_move(start,dest):
#    """
#    Cheking - is move availible for pawn
#    returns True or False
#    >>>check_pawn_move([6,4],[5,4])
#    >>>True
#    >>>check_pawn_move([6,4],[1,4])
#    >>>False
#    """

    return get_figure(board, start[0], start[1]) in "Pp" and get_figure(board, dest[0], dest[1]) == 0 and \
           start[0] == dest[0] and start[1] - dest[1] == 0


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

def check_horizontal(coords):
    """
    Get horizontal figure
    >>> check_gorizontal('a1')
    ['R', 'K', 'B', 'Q', 'M', 'B', 'K', 'R']
    >>> check_gorizontal('a2')
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']
    >>> check_gorizontal('a6')
    [0, 0, 0, 0, 0, 0, 0, 0]
    """
#   this is create test boards
    board = create_default_position(init_board())
    return board[convert_coords_to_indexes(coords)[0]]

if __name__ == '__main__':
    board = create_default_position(init_board())
    while True:
        action = raw_input("?")
        if action in 'Qq':
            break
        try:
            indexes = convert_coords_to_indexes(action)
        except ValueError as e:
            print e
            continue
        print get_figure(board, indexes[0], indexes[1])
