

class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        F = {}

        for i in range(len(s)):
            F[(i,i)] = 1

        for j in range(1,len(s)):
            for i in range(len(s)-j):
                x = F[(i,i+j-1)]
                y = F[(i+1,i+j)]

                if x == y and x == j:
                    if s[i] == s[i+j]:
                        F[(i,i+j)] = x
                    else:
                        F[(i,i+j)] = x + 1
                else:
                    F[(i,i+j)] = max(x,y)
        return F[(0,len(s)-1)]
