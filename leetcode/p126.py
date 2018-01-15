def newStates(old,current,wordList):
    #old is {'word':parent 1, parent 2...}
    #current is {'word':parent 1, parent 2...}
    #wordList is {'word':adjacent word 1, adjacent word 2}
    new  = {}

    for currentWord in current:
        if currentWord in wordList:
            for newWord in wordList[currentWord]:
                if newWord not in current and newWord not in old:
                    if newWord not in new:
                        new[newWord] = [currentWord]
                    else:
                        new[newWord].append(currentWord)

    old.update(current)

    return new

def subHash(wordList):

    edge = {}
    for word1 in wordList:
        for word2 in wordList:
            if word1 != word2:
                for char in xrange(len(word1)):
                    if word1[:char]+word1[char+1:] == word2[:char]+word2[char+1:]:
                        if word1 not in edge:
                            edge[word1] = [word2]
                        else:
                            edge[word1].append(word2)
                        break
            #if match == 1:

    return edge

def forwardPath(beginWord,endWord,wordList):
    if beginWord in wordList:
        wordEdge = subHash(wordList)
    else:
        wordEdge = subHash(wordList+[beginWord])
    if not wordEdge:
        return []
    old = {}
    current = {beginWord : []}
    while current:
        current = newStates(old,current,wordEdge)
        if endWord in current:
            ladder = []
            backwardPath(old,endWord,current[endWord],[],ladder)
            for ladders in ladder:
                ladders.reverse()
            return ladder

    return []

def backwardPath(old,node,parents,path,ladder):
    path.append(node)

    if not parents:
        ladder.append(path)
        return
    paths = [path[:] for x in xrange(len(parents))]
    for index,parent in enumerate(parents):
        backwardPath(old,parent,old[parent],paths[index],ladder)
    return



beginWord = "a"
endWord = "c"
wordList = ['a','b','c']
print forwardPath(beginWord,endWord,wordList)

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print forwardPath(beginWord,endWord,wordList)
