def inorderBT(root,tree):
    if root.left != None:
        inorderBT(root.left,tree)
    tree.append(root.val)

    if root.right != None:
        inorderBT(root.right,tree)
