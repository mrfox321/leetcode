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

def wildCard(string1,string2):
    if not string1 and not string2:
        return True

    if not string1:
        for char in string2:
            if char != '*':
                return False
        return True

    if not string2:
        for char in string1:
            if char != '*':
                return False
        return True

    if (len(string1) == 1 and string1[0] == '*') or (len(string2) == 1 and string2[0] == '*'):
        return True


    #standard char comparison
    if string1[0] not in ['?','*'] and string2[0] not in ['?','*']:
        if string1[0] == string2[0]:
            return wildCard(string1[1:],string2[1:])
        else:
            return False

    if (string1[0] == '?' and string2[0] != '*') or (string2[0] == '?' and string1[0] != '*'):
        return wildCard(string1[1:],string2[1:])

#    if string1[0] == '*' and string2[0] != '*':
#        search_space = [wildCard(string1[1:],string2[i:]) for i in xrange(len(string2))]
#        if True in search_space:
#            return True
#        else:
#            return False

    if string2[0] == '*' and string1[0] != '*':
        search_space = [wildCard(string1[i:],string2[1:]) for i in xrange(len(string1))]
        if True in search_space:
            return True
        else:
            return False

#    if string1[0] == '*' and string2[0] == '*':
#        search_space_1 = [wildCard(string1[1:],string2[i:]) for i in xrange(len(string2))]
#        search_space_2 = [wildCard(string2[1:],string1[i:]) for i in xrange(len(string1))]
#        if True in search_space_1 or True in search_space_2:
#            return True
#        else:
#            return False

x = "aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba"
y = "*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*"
x,y = truncate(x,y)
print wildCard(x,y)
