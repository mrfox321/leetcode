def longR(s,k):

    if k <= 1:
        return len(s)

    if len(s) < k:
        return 0


    freq = {}
    for char in s:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1

    #partition string
    i = 0
    j = 0
    score = 0
    while i < len(s):

        if freq[s[i]] >= k:
            j = i+1
            if j == len(s):
                return score

            while j < len(s):
                if freq[s[j]] >= k:
                    j += 1
                else: #not a match
                    break
            if j-i == len(s):
                return len(s)
            else:
                score = max(score,longR(s[i:j],k))
            i = j+1
        else:
            i += 1

    return score

print longR("a",1)
