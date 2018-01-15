def binary_cut(array,target,start):
    if len(array) < 4:
        for i in xrange(len(array)):
            if target == array[i]:
                return start+i
        return -1

    center = len(array)//2
    if array[0] <= target and target <= array[center]:
        return binary_cut(array[0:center+1],target,start)
    else:
        return binary_cut(array[center+1:],target,start+center+1)

def weird_cut(array,target,start):
    if len(array) < 4:
        for i in xrange(len(array)):
            if target == array[i]:
                return start+i
        return -1
    center = len(array)//2
    left = array[0:center+1]
    right = array[center+1:]

    if left[0] < left[-1]: #if left side is sorted
        if left[0] <= target and target <= left[-1]: #if target is in sorted side
            return binary_cut(left,target,start)
        else: #if target is in weird side
            return weird_cut(right,target,start+center+1)
    else: #if right side is sorted
        if right[0] <= target and target <= right[-1]:
            return binary_cut(right,target,start+center+1)
        else:
            return weird_cut(left,target,start)
