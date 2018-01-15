def longRepeat(s,k):
    if k > len(s):
        return 0
    if k <= 1:
        return len(s)
    if len(s) == 1:
        return 1


    freq = {}

    for char in s:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1

    i = 0
    j = 0
    score = 0

    while i < len(s):
        if freq[s[i]] >= k:
            hfreq = {}
            hfreq[s[i]] = 1

            j = i+1
            if j == len(s):
                return score #at best this is a score of 1, which would be recorded already

            while j < len(s):
                if freq[s[j]] >= k:
                    if s[j] in hfreq:
                        hfreq[s[j]] += 1
                    else:
                        hfreq[s[j]] = 1
                    j += 1
                    if j == len(s): #see if word scores
                        space = [values for values in hfreq.values() if values < k]
                        if not space: #valid substring
                            score = max(score,j-i)
                else: #no match
                    space = [values for values in hfreq.values() if values < k]
                    if not space:
                        score = max(score,j-i)






    while i < len(s):
        if freq[s[i]] >= k:
            j = i+1
            if j == len(s):
                score = max(score,j-i)
                return score
            while j < len(s):
                if freq[s[j]] >= k:
                    j += 1
                    if j == len(s):
                        score = max(score,len(s)-i)
                        return score
                else: #char is under freq threshold
                    score = max(score,j-i)
                    i = j+1
                    break
        else:
            i += 1

    return score




print longRepeat("ababacb",3)
