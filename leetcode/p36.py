def checkDup(row):
    check = {}
    for symbol in row:
        if symbol != '.':
            if symbol not in check:
                check[symbol] = 1
            else:
                return False
    return True

def checkRow(board):

    for i in xrange(9):
        row = board[i]
        if not checkDup(row):
            return False

    return True

def checkCol(board):

    for i in xrange(9):
        col = [board[j][i] for j in xrange(9)]
        if not checkDup(col):
            return False
    return True

def checkBlock(board):

    for i in xrange(3):
        for j in xrange(3):
            block = [board[x][y] for x in xrange(3*i,3*i+3) for y in xrange(3*j,3*j+3)]
            if not checkDup(block):
                return False

    return True

def validSudoku(board):

    if checkRow(board) and checkCol(board) and checkBlock(board):
        return True

    return False
