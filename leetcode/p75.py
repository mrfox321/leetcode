import random as rand

def sortColors(flag):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if len(flag) == 1:
        return flag
    i = 0
    for k in xrange(len(flag)):
        if flag[k] == 0:
            flag[i+1:k+1],flag[i] = flag[i:k],flag[k]
            i += 1
        elif flag[k] == 1:
            flag[i+1:k+1],flag[i] = flag[i:k],flag[k]
    return flag
#flag = [2,1,1,1,1,1,1,0]
flag = [rand.randint(0,2) for i in xrange(1000)]
print flag
sortColors(flag)
print flag
