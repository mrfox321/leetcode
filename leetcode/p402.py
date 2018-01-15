def removeK(num,k):
    ans = []
    while True:
        if k==len(num):
            break
        if k==0:
            ans.append(num)
            break
        new = min(num[:k+1])
        index = num.index(new)

        ans.append(new)

        num = num[index+1:]
        k += -index

    string1 = ''
    for string in ans:
        string1 += string

    for index,char in enumerate(string1):
        if char != '0':
            return string1[index:]

    return '0'

num = "12000"
ans = ''
k = 2
print removeK(num,k)
