def isBST(root):
    if root == None:
        return True

    if isBST(root.left):
        if isBST(root.right):
            if root.val > maxTree(root.left):
                if root.val < minTree(root.right):
                    return True
    return False


def maxTree(root):
    if root == None:
        return -23098230982

    if root.left == None and root.right == None:
        return root.val

    if root.left == None and root.right != None:
        return max(root.val,maxTree(root.right))

    if root.left != None and root.right == None:
        return max(root.val,maxTree(root.left))

    return max(root.val,maxTree(root.left),maxTree(root.right))

def minTree(root):
    if root == None:
        return 23098230982

    if root.left == None and root.right == None:
        return root.val

    if root.left == None and root.right != None:
        return min(root.val,maxTree(root.right))

    if root.left != None and root.right == None:
        return min(root.val,maxTree(root.left))

    return min(root.val,maxTree(root.left),maxTree(root.right))
