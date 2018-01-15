def pathFind(root,goal_sum,path,paths):

    path.append(root.val)
    if sum(path) == goal_sum and root.left == None and root.right == None:
        paths.append(path)
        return
    path_left = path[:]
    path_right = path[:]

    if root.left != None:
        pathSum(root.left,goal_sum,path_left,paths)

    if root.right != None:
        pathSum(root.right,goal_sum,path_right,paths)
