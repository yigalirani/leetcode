class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #improved upon previus attempt by not using addional memoty
        n=len(nums)
        if n<=1: return n
        ans=0
        for i in range(1,n):
            if nums[i]!=nums[ans]:
                ans+=1
            nums[ans]=nums[i]
        return ans+1        