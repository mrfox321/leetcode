def primeDNA(s):

    count = 0

    for index,char in enumerate(s):
        if char == 'A':
            count += 1*10**index
        elif char == 'C':
            count += 2*10**index
        elif char == 'G':
            count += 3*10**index
        elif char == 'T':
            count += 4*10**index
    return count


def findDNA(s):

    if len(s) <= 10:
        return []


    hashDNA = {}
    repeats = []
    for i in xrange(len(s)-9):
        mapping = primeDNA(s[i:i+10])
        if mapping in hashDNA:
            hashDNA[mapping].append(i)
        else:
            hashDNA[mapping] = [i]

    for key,value in hashDNA.items():
        if len(value) > 1:
            repeats.append(s[value[0]:value[0]+10])

    return repeats

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print findDNA(s)
