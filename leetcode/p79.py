def wordSearch(board,word):

    m = len(board)
    n = len(board[0])

    for i in xrange(m):
        for j in xrange(n):
            path = {}
            if subSearch(board,i,j,path,word):
                return True
    return False


def subSearch(board,i,j,path,word):
    if board[i][j] == word[0] and (i,j) not in path:
        if len(word) == 1:
            return True

        path[(i,j)] = 1
        #move right
        if j<len(board[0]) - 1:
            path_right = path.copy()
            if subSearch(board,i,j+1,path_right,word[1:]):
                return True
        #move left
        if j > 0:
            path_left = path.copy()
            if subSearch(board,i,j-1,path_left,word[1:]):
                return True
        #move up
        if i<len(board) - 1:
            path_up = path.copy()
            if subSearch(board,i+1,j,path_up,word[1:]):
                return True
        #move down
        if i > 0:
            path_down = path.copy()
            if subSearch(board,i-1,j,path_down,word[1:]):
                return True

    return False
