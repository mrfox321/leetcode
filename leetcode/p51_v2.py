def isValid(q_list,i,j):

    for queen in q_list:
        if i == queen[0] or j == queen[1] or i-j == queen[0]-queen[1] or i+j == queen[0]+queen[1]:
            return False
    return True

def nQueens(q_list,N,solutions):


    if len(q_list) == N:
        solution = ['Q'.join(['.'*(move[1]),'.'*(N-move[1]-1)]) for move in q_list]
        solutions.append(solution)

    if not q_list:
        row = 0
    else:
        row = q_list[-1][0]+1

    for j in xrange(N):
        if isValid(q_list,row,j):
            q_copy = q_list[:]
            q_copy.append((row,j))
            nQueens(q_copy,N,solutions)
            del q_copy

    return

solutions = []
nQueens([],8,solutions)
print solutions
