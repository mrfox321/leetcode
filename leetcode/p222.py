def goLR(root,string,direction):

    if direction == 'left':
        if root.left == None:
            return (int(string,2),len(string)-1)
        else:
            return goLR(root.left,string+'0',direction)

    if direction == 'right':
        if root.right == None:
            return (int(string,2),len(string)-1)
        else:
            return goLR(root.right,string+'1',direction)

def goTree(root,string):
        if not string:
            if root.left == None and root.right == None:
                return True
            else:
                return False

        if string[0] == '0':
            if root.left != None:
                return goTree(root.left,string[1:])
            else:
                return False
        else:
            if root.right != None:
                return goTree(root.right,string[1:])
            else:
                return False

def countTree(root):

    left = goLR(root,'1','left')
    right = goLR(root,'1','right')

    print left,right

    if right[0] >= left[0]:
        return right[0]

    level = left[1]

    if level == 1:
        return left[0]

    left = left[0]
    right = 2*2**level - 1

    center = (left+right)//2


    while True:

        if right - left < 3:
            score = left
            for i in xrange(left+1,right+1):
                print i
                if goTree(root,bin(i)[3:]):
                    score = i
            return score

        if goTree(root,bin(center)[3:]):
            left = center
            center = (left+right)//2

        else:
            right = center
            center = (left+right)//2
