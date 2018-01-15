def earlyStop(string1,string2):
    if string2[0] == '*' and string2[-1] == '*':
        if '*' not in string2[1:-1] and len(string2[1:-1]) <= len(string1):
            for i in xrange(len(string1)-len(string2[1:-1])+1):
                if string1[i:i+len(string2[1:-1])] == string2[1:-1]:
                    return True
            return False
    return



def truncate(string1,string2):

    ling1 = list(string1)
    ling2 = list(string2)

    i = 0
    while i < len(ling1)-1:
        while ling1[i] == ling1[i+1] and ling1[i] == '*':
             del ling1[i+1]
             if i+1 == len(ling1):
                 break
        i += 1

    i = 0
    while i < len(ling2)-1:
        while ling2[i] == ling2[i+1] and ling2[i] == '*':
            del ling2[i+1]
            if i+1 == len(ling2):
                break
        i += 1

    return ''.join(ling1),''.join(ling2)


def wildCard(i,j,string1,string2,table):

    if (i,j) in table:
        return table[i,j]

    if not string1[i:] and not string2[j:]:
        table[i,j] = True
        return True

    if not string1[i:]:
        if string2[j] == '*':
            table[i,j] = wildCard(i,j+1,string1,string2,table)
            return table[i,j]
        else:
            table[i,j] = False
            return table[i,j]

    if not string2[j:]:
        table[i,j] = False
        return table[i,j]

    if len(string2[j:]) == 1 and string2[j] == '*':
        for k in xrange(len(string1)+1):
            table[k,j] = True
        return table[i,j]

    #standard char comparison
    if string2[j] not in ['?','*']:
        if string1[i] == string2[j]:
            table[i,j] = wildCard(i+1,j+1,string1,string2,table)
            return table[i,j]
        else:
            table[i,j] = False
            return table[i,j]

    #single ? match
    if string2[j] == '?':
        table[i,j] = wildCard(i+1,j+1,string1,string2,table)
        return table[i,j]

    if string2[j] == '*':
        search_space = [wildCard(i+k,j+1,string1,string2,table) for k in xrange(len(string1)-i+1)]
        if True in search_space:
            table[i,j] = True
            return table[i,j]
        else:
            table[i,j] = False
            return table[i,j]

x = "aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba"
y = "*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*"
x,y = truncate(x,y)
table = {}
print wildCard(0,0,x,y,table)
