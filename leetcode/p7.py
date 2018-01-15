class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        elif x < 0:
            sign = -1
        elif x > 0:
            sign = 1

        string = str(abs(x))
        string = string[::-1]

        y = sign*int(string)

        if y >= -2**31 and y<= 2**31-1:
            return y
        else:
            return 0
