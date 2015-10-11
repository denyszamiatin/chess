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


def check_vertical(board, coords):
    """
    Get horizontal figure
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
        if row[coll] != '.':
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
    {(0, 1): 'k', (0, 0): 'r', (0, 7): 'r', (0, 6): 'k', (0, 5): 'b', (0, 4): 'm', (0, 3): 'q', (0, 2): 'b'}
    """

    figures_on_horizontal = {}
    row, column = convert_coords_to_indexes(coordinate)

    for column in range(0, BOARD_SIZE):
        figure = get_figure(board, row, column)

        if figure != '.':
            figures_on_horizontal[(row, column)] = figure

    return figures_on_horizontal


def check_diagonal(board, row, column):

    i = row
    j = column
    while (0 <= i < BOARD_SIZE) and (0 <= j < BOARD_SIZE):
        i += 1
        j += 1
        if i == 8 or i == -1:
            break
        if j == 8 or j == -1:
            break

        diagonal_result1.append(get_figure(board,i,j))

    i = row
    j = column
    while (0 <= i < BOARD_SIZE) and (0 <= j < BOARD_SIZE):
        i += 1
        j -= 1
        if i == 8 or i == -1:
            break
        if j == 8 or j == -1:
            break
        diagonal_result2.append(get_figure(board,i,j))

    i = row
    j = column
    while (0 <= i < BOARD_SIZE) and (0 <= j < BOARD_SIZE):
        i -= 1
        j += 1
        if i == 8 or i == -1:
            break
        if j == 8 or j == -1:
            break
        diagonal_result3.append(get_figure(board,i,j))

    i = row
    j = column
    while (0 <= i < BOARD_SIZE) and (0 <= j < BOARD_SIZE):
        i -= 1
        j -= 1
        if i == 8 or i == -1:
            break
        if j == 8 or j == -1:
            break
        diagonal_result4.append(get_figure(board,i,j))


    #print diagonal_result1
    #print diagonal_result2
    #print diagonal_result3
    #print diagonal_result4

    diagonal_result = diagonal_result1 + diagonal_result2 + diagonal_result2 + diagonal_result3

    return diagonal_result


if __name__ == '__main__':
    import doctest
    doctest.testmod()

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
