class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        area = min(height[1],height[0])
        for index in xrange(2,len(height)):
            area1 = (index-i)*min(height[index],height[i])
            area2 = (index-j)*min(height[index],height[j])

            if max(area1,area2) > area:
                if area1 >= area2:
                    j = index
                    area = area1
                else:
                    i = index
                    area = area2
        return area
