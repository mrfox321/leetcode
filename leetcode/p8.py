class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if abs(x) < 10:
            return True
        i = 0
        F = []
        while x//10**i != 0:
            F.append(x%10**(i+1)//10**i)
            i += 1
        if F==F[::-1]:
            return True
        else:
            return False

            
