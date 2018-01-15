def outPath(root,state,goal1,goal2,finalstring,trigger):

    if root is goal1 or root is goal2:
        finalstring[trigger[0]] = ''.join(state)
        print root.val,state,finalstring,trigger[0]
        if trigger[0] == 0: #found first node
            trigger[0] += 1
        else: #found both nodes
            return

    if root.left is not None:
        state.append('0')
        outPath(root.left,state,goal1,goal2,finalstring,trigger)
        state.pop()
    if root.right is not None:
        state.append('1')
        outPath(root.right,state,goal1,goal2,finalstring,trigger)
        state.pop()


def goTree(root,string):
    if not string:
        return root

    if string[0] == '0':
        return goTree(root.left,string[1:])

    else:
        return goTree(root.right,string[1:])

def compareString(string1,string2):
    if not string1 or not string2:
        return ''

    for i in xrange(max(len(string1),len(string2))):
        if string1[i] != string2[i]:
            return string1[:i]

def LCA(root,p,q):

    string = ['','']
    print string
    outPath(root,[],p,q,string,[0])

    string3 = compareString(string[0],string[1])

    return goTree(root,string3)
