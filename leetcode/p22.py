def check(left,right,count,answer,string):
    if left == 0 and right == 0 and count == 0:
        answer.append(string)
        return
    elif left == 0 and right == 0 and count != 0:
        return

    if count > 0 and left > 0:
        check(left-1,right,count-1,answer,string+')')
    if right > 0:
        check(left,right-1,count+1,answer,string+'(')

answer = []
check(4,4,0,answer,'')
print answer
