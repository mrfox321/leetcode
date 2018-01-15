def binsum(root,rootsum):

    if root.left is None and root.right is None:
        rootsum.val = root.val
        return

    if root.left is not None and root.right is None:
        rootsum.left = TreeNode(None)
        binsum(root.left,rootsum.left)

        rootsum.val = root.val + rootsum.left.val
        return

    if root.left is  None and root.right is not None:
        rootsum.right = TreeNode(None)
        binsum(root.right,rootsum.right)

        rootsum.val = root.val + rootsum.right.val
        return

    if root.left is not None and root.right is not None:
        rootsum.left = TreeNode(None)
        binsum(root.left,rootsum.left)

        rootsum.right = TreeNode(None)
        binsum(root.right,rootsum.right)

        rootsum.val = root.val + rootsum.right.val + rootsum.left.val

        return

def equalCut(root,rootsum):


    c = root.val
    while root.left is not None and root.right is not None:
        if root.left is None:
            b = 0
            a = rootsum.right.val
            node = root.right
            nodesum = rootsum.right
        elif root.right is None:
            b = 0
            a = rootsum.left.val
            node = root.left
            nodesum = rootsum.left
        else:
            else:
                a = max(rootsum.left.val,rootsum.right.val)
                b = min(rootsum.left.val,rootsum.right.val)
                if rootsum.left.val == a:
                    node = root.left
                    nodesum = rootsum.left
                else:
                    node = root.right
                    nodesum = rootsum.right

        if b + c == a:
            return True

        elif b + c > a:
            return False

        else:
            c += b + node.val
            root = node
            rootsum = nodesum

    return False
