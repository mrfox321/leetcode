class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.thing = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        self.put(word,self.thing)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False

        root = self.thing
        for char in word:
            if char in root:
                index,root = root[char][0],root[char][1]
            else:
                return False

        if index == 0:
            return False
        else:
            return True


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if not prefix:
            return False

        root = self.thing
        for char in prefix:
            if char in root:
                root = root[char][1]
            else:
                return False

        return True

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

obj = Trie()
obj.insert('sexy')
print obj.search('sex')
print obj.startsWith('sex')
