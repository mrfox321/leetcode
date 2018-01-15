def canPart(string,wordDict,table):

    if string in table:
        return table[string]
    if not string:
        table[string] = True
        return True

    space = []
    for i in xrange(len(string)+1):
        if string[:i] in wordDict:
            space.append(canPart(string[i:],wordDict,table))

    if True in space:
        table[string] = True
        return True
    table[string] = False
    return False


s="acaaaaabbbdbcccdcdaadcdccacbcccabbbbcdaaaaaadb"
wordDict = ["abbcbda","cbdaaa","b","dadaaad","dccbbbc","dccadd","ccbdbc","bbca","bacbcdd","a","bacb","cbc","adc","c","cbdbcad","cdbab","db","abbcdbd","bcb","bbdab","aa","bcadb","bacbcb","ca","dbdabdb","ccd","acbb","bdc","acbccd","d","cccdcda","dcbd","cbccacd","ac","cca","aaddc","dccac","ccdc","bbbbcda","ba","adbcadb","dca","abd","bdbb","ddadbad","badb","ab","aaaaa","acba","abbb"]
table = {}
print canPart(s,wordDict,table)
