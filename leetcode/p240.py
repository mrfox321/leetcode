def search2D(matrix,target):

    row_lo = 0
    row_hi = len(matrix)

    col_lo = 0
    col_hi = len(matrix[0])

    while True:
        #row search
        rows = []
        for i in xrange(row_lo,row_hi):
            if matrix[i][col_lo] <= target:
                if target <= matrix[i][col_hi-1]:
                    if target == matrix[i][col_lo] or target == matrix[i][col_hi-1]:
                        return True
                    rows.append(i)

        if not rows:
            return False
        row_lo = rows[0]
        row_hi = rows[-1]+1

        #col search
        cols = []
        for i in xrange(col_lo,col_hi):
            if matrix[row_lo][i] <= target:
                if target <= matrix[row_hi-1][i]:
                    if target == matrix[row_lo][i] or target == matrix[row_hi-1][i]:
                        return True
                    cols.append(i)

        if not cols:
            return False
        col_lo = cols[0]
        col_hi = cols[-1]+1

        if len(rows) == 1 and len(cols) == 1:
            if matrix[rows[0]][cols[0]] == target:
                return True

            else:
                return False


matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

target = 25
print search2D(matrix,target)
