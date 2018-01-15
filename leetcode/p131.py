def isPalindrome(string):
    center = len(string)//2
    if len(string) == 1:
        return True
    if len(string)%2 == 1: #odd:
        if string[:center] == string[-1:center:-1]:
            return True
    else: #even
        string[:center],string[center:]
        if string[:center] == string[-1:center-1:-1]:
            return True


def palindromePartition(string):
    #initialize
    partition = [[string[0]]]
    for char in string[1:]:
        new_partition = []
        for dum in partition:
            if len(dum) == 1:
                new_partition.append([dum[0],char])
                if isPalindrome(dum[0]+char):
                    new_partition.append([dum[0]+char])
            else:
                new_partition.append(dum+[char])
                if isPalindrome(dum[-1]+char):
                    new_partition.append(dum[:-1]+[dum[-1]+char])
                if not isPalindrome(dum[-2]+dum[-1]):
                    if isPalindrome(dum[-2]+dum[-1]+char):
                        new_partition.append(dum[:-2]+[dum[-2]+dum[-1]+char])
        partition = new_partition
    return partition

print palindromePartition('cabba')
