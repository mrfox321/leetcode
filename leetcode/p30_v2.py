def hashWords(words):
    hashword = {}
    for key in words:
        if key not in hashword:
            hashword[key] = 1
        else:
            hashword[key] += 1
    return hashword

def findSubSub(s,hashword,start,word_len):
    if sum(hashword.itervalues()) == 0:
        return start

    if s[start:start+word_len] not in hashword:
        return

    else:
        if hashword[s[start:start+word_len]] == 0: #no more capacity
            return
        else:
            hashword[s[start:start+word_len]] += -1
            return findSubSub(s[word_len:],hashword,start,word_len)

def findSub(s,words,word_len):
    hashword = hashWords(words)
    start = 0
    string_len = sum(hashword.itervalues())*word_len
    sub = []
    match = 0
    while start <= len(s)-string_len:
        dummyhash = hashWords(words)
        if match == 0:
            output = findSubSub(s,dummyhash,start,word_len)
        else:
            output = start
        if output == None:
            start += word_len
        else: #successful answer
            sub.append(output)
            if s[start:start+word_len] == s[start+string_len:start+string_len+word_len]:
                match = 1
                start += word_len
            else:
                match = 0
                if s[start+string_len:start+string_len+word_len] not in hashword:
                    start = start+string_len+word_len
                else:
                    start += word_len
    return sub

def findSubstring(s,word_list):
    word_len = len(word_list[0])
    solution = []
    for offset in xrange(word_len):
        for index in findSub(s[offset:],word_list,word_len):
            solution.append(offset+index)
    return solution

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]

#print findSubSub(s,hashWords(words),2,len(words[0]))
print findSubstring(s,words)
