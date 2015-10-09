board = [[int(0) for x in xrange(8)] for y in xrange(8)]
vertical = []
board[0] = ['r', 'k', 'b', 'q', 'm', 'b', 'k', 'r']
board[1] = ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p']
board[6] = ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']
board[7] = ['R', 'K', 'B', 'Q', 'M', 'B', 'K', 'R']
coord1 = int(raw_input("1?"))
coord2 = int(raw_input("2?"))

if coord2 > coord1:
    X = coord2 - coord1
elif coord1 > coord2:
    X = coord1 - coord2
else:
    X = 0

y = 0
i = 0
while y < 8 - X:
    if coord2 > coord1:
        if board[coord1 - coord1 + i][coord2 - coord1 + i] <> 0:
            vertical.append(board[coord1 - coord1 + i][coord2 - coord1 + i])
            y += 1
            i += 1
        else:
            y += 1
            i += 1
    if coord1 > coord2:
        if board[coord1 - coord2 + i][coord2 - coord2 + i] <> 0:
            vertical.append(board[coord1 - coord2 + i][coord2 - coord2 + i])
            y += 1
            i += 1
        else:
            y += 1
            i += 1
    if coord1 == coord2:
        if board[0 + i][0 + i] <> 0:
            vertical.append(board[0 + i][0 + i])
            y += 1
            i += 1
        else:
            y += 1
            i += 1
print vertical
