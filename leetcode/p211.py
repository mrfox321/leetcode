class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.thing = {}


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.put(word,self.thing)


    def subSearch(self,word,root):

        char = word[0]

        if char != '.':
            if char in root:
                if len(word) == 1: #end of word
                    if root[char][0] == 1:
                        return True
                    else:
                        return False
                else: #go deeper
                    return self.subSearch(word[1:],root[char][1])


            else: #char not in root
                return False

        else:  #char == '.'
            if root:  #if there are paths
                if len(word) == 1:
                    space = [root[char][0] for char in root]
                    if 1 in space:
                        return True
                    else:
                        return False

                else:
                    space = [self.subSearch(word[1:],root[char][1]) for char in root]
                    if True in space:
                        return True
                    else:
                        return False
            else:
                return False

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.subSearch(word,self.thing)




    def put(self,word,root):

        if word[0] not in root:
            if len(word) == 1:
                root[word[0]] = [1,{}]
                return
            else:
                root[word[0]] = [0,{}]
                self.put(word[1:],root[word[0]][1])

        elif word[0] in root:
            if len(word) == 1:
                root[word[0]][0] = 1
                return
            else:
                self.put(word[1:],root[word[0]][1])


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('word')
print obj.search('....')
