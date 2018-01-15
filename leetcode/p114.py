def flattens(root):
    #no children
    if root.left is None and root.right is None:
        return root

    #if there is 1 child
    if root.left is None and root.right is not None:
        right_end = flattens(root.right)
        return right_end

    if root.left is not None and root.right is None:
        root.right = root.left
        root.left = None
        right_end = flattens(root.right)
        return right_end


    #if there are 2 children
    root.left,root.right = root.right,root.left

    right_end = flattens(root.right)
    left_end = flattens(root.left)
    right_end.right = root.left
    root.left = None
    return left_end
