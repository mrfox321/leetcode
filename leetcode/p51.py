def moveTable(q_list,N):

    table = {}

    for i in xrange(N):
        for j in xrange(N):
            table[i,j] = 1
    if not q_list:
        moves = [(i,j) for i in xrange(N) for j in xrange(N)]
        return moves

    for queen in q_list: #(i,j) coordinate
        #row mask and column
        for i in xrange(N):
            table[queen[0],i] = 0
            table[i,queen[1]] = 0
        #diagonal mask
        for i in xrange(-7,8):
            if queen[0] + i >= 0 and queen[0] + i < N:
                if queen[1] + i >= 0 and queen[1] + i < N:
                    table[queen[0]+i,queen[1]+i] = 0
                if queen[1] + i >= 0 and queen[1] - i < N:
                    table[queen[0]+i,queen[1]-i] = 0

    last_queen = q_list[-1]
    moves = []
    #make a list of viable moves beyond the last queen
    for i in xrange(last_queen[0]+1,N): #cannot be on row of last queen
        for j in xrange(N):
            if table[i,j] == 1:
                moves.append((i,j))

    return moves


def nQueens(q_list,N,solutions):

    if len(q_list) == N:
        solution = ['Q'.join(['.'*(move[1]),'.'*(N-move[1]-1)]) for move in q_list]
        solutions.append(solution)

    moves = moveTable(q_list,N)
    if moves:
        for move in moves:
            q_copy = q_list[:]
            q_copy.append(move)
            nQueens(q_copy,N,solutions)
            del q_copy

    return


#print moveTable([(1,1)],8)
solutions = []
nQueens([],8,solutions)
print solutions
