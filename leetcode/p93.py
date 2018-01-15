def ipTree(before,current,answer,dots):
    if current:
        if dots == 0:
            if int(current) <= 255:
                if len(current) > 1 and current[0] != '0':
                    answer.append(before+current)
                elif len(current) == 1:
                    answer.append(before+current)
        for i in xrange(3):
            if int(current[0:i+1]) <= 255:
                if i > 0 and current[0] != '0':
                    new_before = before+current[0:i+1]+'.'
                    new_current = current[i+1:]
                    ipTree(new_before,new_current,answer,dots-1)
                elif i == 0:
                    new_before = before+current[0:i+1]+'.'
                    new_current = current[i+1:]
                    ipTree(new_before,new_current,answer,dots-1)

s = '25525511135'
answer = []

print int('0000')
