def outPath(root,string_list,goal,finalstring):
    if root is goal:
        finalstring[0] = ''.join(string_list)
        return
    string1 = string_list[:]
    string2 = string_list[:]
    del string_list
    if root.left != None:
        string1.append('0')
        outPath(root.left,string1,goal,finalstring)
    if root.right != None:
        string2.append('1')
        outPath(root.left,string2,goal,finalstring)

def outPath(root,string,goal,finalstring):
    if root is goal:
        finalstring[0] = string
        return

    if root.left != None:
        outPath(root.left,string+'0',goal,finalstring)
    if root.right != None:
        outPath(root.right,string+'1',goal,finalstring)

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

    return string1[:count+1]
def LCA(root,p,q):

    string1 = ['']
    string1 = outPath(root,[],p,string1)
    string2 = ['']
    string2 = outPath(root,[],q,string2)

    string3 = compareString(string1[0],string2[0])

    return goTree(root,string3)
