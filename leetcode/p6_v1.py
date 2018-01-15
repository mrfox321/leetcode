class Solution(object):
    def convert(self, s, numRows):

        if len(s) <= numRows or numRows == 1:
            return s

        F = {}
        row_index = 0
        count = -1
        for i in xrange(len(s)):
            print i,row_index,numRows-1
            if i<=numRows-1:
                F[i] = s[i]
            else:
                F[row_index] += s[i]
            if row_index == 0 or row_index == numRows-1:
                count *= -1
            row_index += count

        strings = F[0]
        for i in xrange(1,len(F)):
            strings += F[i]

        return strings
