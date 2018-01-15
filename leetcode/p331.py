def isPre(s,index):
    print index
    if index == len(s) - 1:
        return index + 1

    if index == len(s) - 3:
        return -1

    if index == len(s) - 5:
        if s[index] == '#':
            return -1


    if index >= len(s):
        return index
    if s[index+2] == '#' and s[index+4] == '#':
        return index + 3

    if s[index+2] == '#':
        return isPre(s,index+2)

    else:
        i = isPre(s,index+1)
        return isPre(s,i)

def isPre(s,index):

    if index == -1:
        return -1
    if s[index] == '#':
        return -1
    if index > len(s)-3:
        return -1

def isPre1(s):

    index = 0

    while index < len(s) - 3:

        if s[index] == '#':
            print 'triple'
            return False

        if s[index+1] == '#' and s[index+2] == '#':
            index += 3
        elif s[index+1] == '#':
            index += 2
        else:
            index += 1

    print index,len(s) - 2
    if index != len(s) - 3:
        return False
    else:
        if s[index] == '#':
            return False
        return True
nums = "9,3,4,#,#,1,#,#,2,#,6,#,#"
s = nums.split(',')
print isPre1(s)
