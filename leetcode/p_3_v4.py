def lengthOfLongestSubstring(s):
    if len(s) <= 1:
        return len(s)

    score = 0
    for i in xrange(len(s)):
        F = set()
        for j in xrange(i,len(s)):
            if s[j] not in F:
                F.add(s[j])
                if j==len(s)-1:
                    score = max(score,len(F))
                    if score == 95:
                        return score
            else:
                score = max(score,len(F))
                if score == 95:
                    return score
                break
    return score

s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "
print lengthOfLongestSubstring(s)
