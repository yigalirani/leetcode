from math import sqrt
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        for width in range(int(sqrt(area)),0,-1):
            height=area/width
            if height*width==area:
                return [height,width]
        