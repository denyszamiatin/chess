__author__ = 'akalinin'
from chessboard import HORIZONTAL_NAMES
from chessboard import VERTICAL_NAMES
from chessboard import convert_indexes_to_coords
FIGURE_TYPES_WHITE = [" ", "wrook", "wknight", "wbishop", "wqeen", "wking", "wbishop", "wknight", "wrook"]
FIGURE_TYPES_BLACK = [" ", "brook", "bknight", "bbishop", "bqeen", "bking", "bbishop", "bknight", "brook"]
PAWNS = ["wpawn", "bpawn"]
HORIZONTAL_INDEXES = '12345678'
VERTICAL_INDEXES = '12345678'
indexes = str(convert_indexes_to_coords())


def get_figure_type(indexes):
    """Returns type of figure
    by coordinates
    >>>get_figure_type(a1):
    "brook"
    """
    h_index = int(HORIZONTAL_INDEXES[HORIZONTAL_NAMES.index(indexes[0])])
    v_index = int(VERTICAL_INDEXES[VERTICAL_NAMES.index(indexes[1])])
    print h_index
    print v_index
    print FIGURE_TYPES_BLACK[int(v_index)]
    figure_type = " "
    if h_index == 1:
        figure_type = FIGURE_TYPES_BLACK[int(v_index)]
    elif h_index == 2:
        figure_type = PAWNS[1]
    elif h_index == 8:
        figure_type = FIGURE_TYPES_WHITE[int(v_index)]
    elif h_index == 7:
        figure_type = PAWNS[0]

    else:
        print "There is no figure"

    return figure_type

