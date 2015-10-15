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
    board[0] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
    board[1] = ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p']
    board[6] = ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']
    board[7] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']

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


def is_white(board, cell):
    return get_figure(board, cell[0], cell[1]).isupper()


def is_black(board, cell):
    return get_figure(board, cell[0], cell[1]).islower()


def get_pawn_direction (board, cell):
    """
    Cheking - is move valid for black or White pawn
    returns True or False
    """
    return -1 if is_white(board, cell) else 1


def is_pawn(board, dest):
    return get_figure(board, dest[0], dest[1]) in "Pp"


def is_empty_cell(board, dest):
    return get_figure(board, dest[0], dest[1]) == EMPTY_CELL


def is_vertical_move(start, dest):
    return start[1] == dest[1]


def get_vertical_distance(start, dest):
    return dest[0] - start[0]


def is_two_cell_move(board, dest, start):
    return all((
        get_vertical_distance(start, dest) == get_pawn_direction(board, start) * 2,
        start[0] in (1, 6),
        is_empty_cell(board, (start[0] + get_pawn_direction(board, start), start[1]))
    ))


def is_one_cell_move(board, dest, start):
    return get_vertical_distance(start, dest) == get_pawn_direction(board, start)


def check_first_pawn_move(board, start, dest):
    """
    Cheking - is first pawn move availible
    returns True or False
    >>> board = create_default_position(init_board())
    >>> check_first_pawn_move(board, [6,4],[4,4])
    True
    >>> check_first_pawn_move(board, [1,4],[3,4])
    True
    >>> check_first_pawn_move(board, [6,4],[5,4])
    True
    >>> check_first_pawn_move(board, [6,4],[1,4])
    False
    >>> check_first_pawn_move(board, [6,4],[3,4])
    False
    >>> check_first_pawn_move(board, [6,4],[3,3])
    False
    """
    return all((
        is_pawn(board, start),
        is_empty_cell(board, dest),
        is_vertical_move(start, dest),
        any((
            is_one_cell_move(board, dest, start),
            is_two_cell_move(board, dest, start)
        ))
    ))


def check_vertical(board, coords):
    """
    Get figures from vertical
    >>> board = create_default_position(init_board())
    >>> check_vertical(board, 'a1')
    {'p': [1, 0], 'R': [7, 0], 'r': [0, 0], 'P': [6, 0]}
    >>> check_vertical(board, 'c2')
    {'p': [1, 2], 'B': [7, 2], 'b': [0, 2], 'P': [6, 2]}
    """
    vertical = {}
    c = convert_coords_to_indexes(coords)
    row = c[0]
    coll = c[1]
    i = 0
    for row in board:
        if row[coll] != EMPTY_CELL:
            vertical[row[coll]] = [i, coll]
        i += 1
    return vertical


def check_horizontal(board, coordinate):
    """
    Get figures from horizontal
    >>> board = create_default_position(init_board())
    >>> check_horizontal(board, 'e2')
    {(6, 4): 'P', (6, 7): 'P', (6, 6): 'P', (6, 1): 'P', (6, 0): 'P', (6, 3): 'P', (6, 2): 'P', (6, 5): 'P'}
    >>> check_horizontal(board, 'e3')
    {}
    >>> check_horizontal(board, 'a8')
    {(0, 1): 'n', (0, 0): 'r', (0, 7): 'r', (0, 6): 'n', (0, 5): 'b', (0, 4): 'k', (0, 3): 'q', (0, 2): 'b'}
    """

    figures_on_horizontal = {}
    row, column = convert_coords_to_indexes(coordinate)

    for column in range(0, BOARD_SIZE):
        figure = get_figure(board, row, column)

        if figure != '.':
            figures_on_horizontal[(row, column)] = figure

    return figures_on_horizontal


def check_diagonal(board, coordinate):
    """
    Get figures from both diagonals
    >>> board = create_default_position(init_board())
    >>> check_diagonal(board, 'a1')
    {(6, 1): 'P', (1, 6): 'p', (0, 7): 'r'}
    >>> check_diagonal(board, 'e4')
    {(0, 0): 'r', (7, 1): 'N', (6, 6): 'P', (7, 7): 'R', (6, 2): 'P', (1, 7): 'p', (1, 1): 'p'}
    >>> check_diagonal(board, 'h7')
    {(0, 6): 'n', (6, 2): 'P', (7, 1): 'N'}
    """

    row, column = convert_coords_to_indexes(coordinate)
    diagonal_result = {}
    steps = ((1, 1), (-1, 1), (1, -1), (-1, -1))
    for x, y in steps:
        i = row
        j = column
        while True:
            i += x
            j += y
            if not 0 <= i < BOARD_SIZE or not 0 <= j < BOARD_SIZE:
                break
            if not is_empty_cell(board, (i, j)):
                diagonal_result[(i, j)] = (get_figure(board,i,j))
    return diagonal_result


def log_move(start, dest, figure, game_name='chessgame001'):
    """
    Writes move to a log file
    >>> log_move('e2', 'e4', 'P')
    'Pe2-e4 '
    >>> log_move('g8', 'f6', 'n')
    'ng8-f6\\n'
    """

    try:
        f = open(game_name, 'w')
    except IOError:
        print "Can't open", game_name

    if figure in ('PRNBQKBNR'):
        notation = figure + start + '-' + dest + ' '
    elif figure in ('prnbqkbnr'):
        notation = figure + start + '-' + dest + '\n'
    else:
        notation = 'No figure detected'

    f.write(notation)
    f.close()
    return notation


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    board = create_default_position(init_board())
    check_first_pawn_move(board, [6,4],[4,4])
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
