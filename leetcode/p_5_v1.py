def longestPalindrome(s):
    if len(s) <= 1:
        return s

    score = 0

    #odd block
    for i in range(len(s)):
        count = 1 #all single char are palindromes
        width = 1
        while True:
            if i-width >= 0 and i+width <= len(s) - 1 and s[i-width] == s[i+width]:
                count += 2
                width += 1
            else:
                if score < count:
                    score = count
                    palindrome = s[i-width+1:i+width]
                break

    #even block
    for i in range(len(s)):
        count = 0 #all single char are palindromes
        width = 0
        while True:
            if i-width >= 0 and i+1+width <= len(s) - 1 and s[i-width] == s[i+1+width]:
                count += 2
                width += 1
            else:
                if score < count:
                    score = count
                    palindrome = s[i-width+1:i+width+1]
                break
    return palindrome
