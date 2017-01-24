class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_here=0
        maxsofar=0
        for x in nums:
            if x==1:
                max_here+=1
                maxsofar=max(maxsofar,max_here)
            else:
                max_here=0
        return maxsofar 