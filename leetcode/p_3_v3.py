

class Solution(object):

    def lengthOfLongestSubstring(self, s):
        max = 0
        for i in range(len(s)):
            F = {}
            for j in range(i,len(s)):
                if s[j] not in F:
                    F[s[j]] = 1
                else:
                    if j-i > max:
                        max = j-i
                        break
        return max
