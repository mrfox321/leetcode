def preIn(pre,ino):

    if not pre:
        return

    root = TreeNode(pre[0])

    if len(pre) == 1:
        return root

    for i in xrange(len(ino)):
        if pre[0] == ino[i]:
            index = i
            break

    root.left = preIn(pre[1:index+1],ino[:index])
    root.right = preIn(pre[index+1:],ino[index+1:])

    return root
