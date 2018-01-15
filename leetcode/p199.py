def rightView(root):
    view = []
    if not root:
        return []

    rView(root,view)
    return view

def rView(root,view):

    level = []
    level.append(root)


    while True:
        next_level = []
        for parent in level:
            if parent.left != None:
                next_level.append(parent.left)
            if parent.right != None:
                next_level.append(parent.right)
            if parent is level[-1]:
                view.append(parent.val)
        if not next_level:
            break
        else:
            level = next_level
