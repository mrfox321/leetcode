

class Solution(object):

    def __init__(self):

        self.string = None
        self.F = {}

    def sub_sub(self,i,j):
        if (i,j) in self.F:
            return self.F[(i,j)]
        else:
            x = self.sub_sub(i,j-1)
            y = self.sub_sub(i+1,j)
            if x == y and x == j - i:
                if self.string[i] == self.string[j]:
                    self.F[(i,j)] = x
                    return x
                else:
                    self.F[(i,j)] = x + 1
                    return x + 1
            else:
                self.F[(i,j)] = max(x,y)
                return max(x,y)


    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.string = s
        for i in xrange(len(s)):
            self.F[(i,i)] = 1 #string with 1 character does not have repeated chars

        return self.sub_sub(0,len(s)-1)
