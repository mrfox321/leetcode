def phoneNum(digits):

    nums = [[''],[''],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]

    letters = ['']
    for num in digits: #num is string (convert to int)
        new_letters = []
        for char in nums[int(num)]:
            for string in letters:
                new_letters.append(string+char)

        letters = new_letters

    return letters

print phoneNum('23')
