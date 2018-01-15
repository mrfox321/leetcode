def sumBST(root,count):
    new_count = count*10 + root.val
    if root.left == None and root.right == None:
        return new_count


    if root.left != None and root.right == None:
        return sumBST(root.left,new_count)

    if root.right != None  and root.left == None:
        return sumBST(root.right,new_count)

    if root.right != None and root.left != None:
        return sumBST(root.left,new_count)+sumBST(root.right,new_count)
