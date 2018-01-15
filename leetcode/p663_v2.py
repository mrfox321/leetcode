def binsum(root,rootsum,table):

    if root.left is None and root.right is None:
        rootsum.val = root.val

        if rootsum.val not in table:
            table[rootsum.val] = 1
        return

    if root.left is not None and root.right is None:
        rootsum.left = TreeNode(None)
        binsum(root.left,rootsum.left)

        rootsum.val = root.val + rootsum.left.val

        if rootsum.val not in table:
            table[rootsum.val] = 1
        return

    if root.left is  None and root.right is not None:
        rootsum.right = TreeNode(None)
        binsum(root.right,rootsum.right)

        rootsum.val = root.val + rootsum.right.val

        if rootsum.val not in table:
            table[rootsum.val] = 1
        return

    if root.left is not None and root.right is not None:
        rootsum.left = TreeNode(None)
        binsum(root.left,rootsum.left)

        rootsum.right = TreeNode(None)
        binsum(root.right,rootsum.right)

        rootsum.val = root.val + rootsum.right.val + rootsum.left.val

        if rootsum.val not in table:
            table[rootsum.val] = 1

        return

class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root.left is None and root.right is None:
            return False
        rootsum = TreeNode(None)
        table = {}
        binsum(root,rootsum,table)
        if rootsum.val%2 == 1:
            return False
        return rootsum.val/2 in table
