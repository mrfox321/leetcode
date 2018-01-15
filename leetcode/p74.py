def searchMatrix(matrix, target):
    if not matrix:
        return False


    mat = []
    for mats in matrix:
        mat += mats
    print mat
    if target < mat[0] or target > mat[-1]:
        return False

    lower = 0
    upper = len(mat)-1
    center = (lower + upper)//2
    while True:
        print lower,center,upper
        if mat[lower] <= target and target <= mat[center]:
            upper = center
            center = (lower + upper)//2
        else:
            lower = center
            center = (lower + upper)//2
        if upper - lower <= 2:
            print lower,upper,mat[lower:upper+1]
            if target in mat[lower:upper+1]:
                return True
            else:
                return False

print searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
],3)
