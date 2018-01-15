def findSubstring(s, word_list):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    w_len = len(word_list[0])
    solution = []
    words = {}
    for word in word_list:
        if word not in words:
            words[word] = 1
        elif word in words:
            words[word] += 1

    for offset in xrange(w_len):
        for index in findSubsub(s[offset:],len(word_list),words,w_len):
            solution.append(offset+index)
    return solution


def findSubsub(s,wordnum,words,w_len):
    subsub = []
    s_len = len(words)*w_len #length of concatenated string
    if s_len > len(s):
        return subsub

    start = 0
    while start <= len(s)-s_len:
        if s[start:start+w_len] in words:
            F = {}
            F[s[start:start+w_len]] = [start]
            if wordnum == 1:
                subsub.append(start)
                start = start + w_len
            else:
                for runner in xrange(1,wordnum):
                    end = start+w_len*runner
                    new_word = s[end:end+w_len]
                    if new_word in words and new_word not in F:
                        F[new_word] = [end]
                        count = 0

                        for key in F:
                            count += len(F[key])
                        if count == wordnum:
                            subsub.append(start)
                            start = start + w_len
                            break
                    elif new_word in words and new_word in F: #include case where duplicate words in list
                        if words[new_word] > len(F[new_word]): #if there is additional capactiy
                            F[new_word].append(end)
                            count = 0
                            for key in F:
                                count += len(F[key])
                            if count == wordnum:
                                subsub.append(start)
                                start = start + w_len
                                break
                            start = start + w_len
                        else: # if there is no more capacity
                            start = F[new_word][0] + w_len
                            break
                    elif new_word not in words:
                        start = end + w_len
                        break
        else:
            start = start + w_len

    return subsub


s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
print findSubstring(s,words)
