def nextRight(root):

    if not root:
        return
    level = [root]
    next_level = []
    while True:
        if len(level) > 1:
            level[0].next = level[1]
            if level[0].left != None:
                next_level.append(level[0].left)
                next_level.append(level[0].right)
            level.pop(0)
        else:
            level[0].next = None
            if level[0].left != None:
                next_level.append(level[0].left)
                next_level.append(level[0].right)
            else:
                return
            level = next_level
            next_level = []
