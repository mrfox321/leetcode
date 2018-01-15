def primeDNA(s):

    count = 0

    for index,char in enumerate(s):
        if char == 'A':
            count += 1*10**(9-index)
        elif char == 'C':
            count += 2*10**(9-index)
        elif char == 'G':
            count += 3*10**(9-index)
        elif char == 'T':
            count += 4*10**(9-index)
    return count

def findDNA(s):

    if len(s) <= 10:
        return []

    hashbit = {'A':1,'C':2,'G':3,'T':4}
    hashDNA = {}
    repeats = []

    mapping = primeDNA(s[:10])
    hashDNA[mapping] = [0]
    print mapping
    for i in xrange(1,len(s)-9):

        mapping -= hashbit[s[i-1]]*10**9
        mapping *= 10
        mapping += hashbit[s[i+9]]
        print mapping

        if mapping not in hashDNA:
            hashDNA[mapping] = [i]
        else:
            if len(hashDNA[mapping]) == 1:
                hashDNA[mapping].append(i)
                repeats.append(s[i:i+10])
            else:
                hashDNA[mapping].append(i)

    return repeats


s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print findDNA(s)
