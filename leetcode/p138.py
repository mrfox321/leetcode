def vote2(nums):
    m = 0
    i = 0
    for num in nums:
        if i == 0:
            m = num
            i = 1
        elif m == num:
                i += 1
        else:
            i += -1

    count = 0
    for num in nums:
        if m == num:
            count += 1
    if count >= 2:
        return [m]

def vote3(nums, exclude):

    m = 0
    i = 0
    for num in nums:
        if i == 0:
            m = num
            i = 2
        elif m == num and m not in exclude:
                i += 2
        else:
            i += -1

    count = 0
    for num in nums:
        if m == num and m not in exclude:
            count += 1

    if count > len(nums)//3:
        exclude.append(m)
    else:
        return

print vote2([2,5,5])

exclude = []
vote3([0,3,4,0],exclude)
print exclude
vote3([0,3,4,0],exclude)
print exclude
