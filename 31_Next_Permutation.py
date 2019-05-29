class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverse(start,end):
            nums[start:end]=nums[start:end][::-1]
        def swap(i,j):
            c=nums[j]
            nums[j]=nums[i]
            nums[i]=c
            
        def find_i():
            for i in range(len(nums)-2,-1,-1):
                if nums[i]<nums[i+1]:
                    return i
            return -1
        i=find_i()
        if i!=-1:
            swap(i,i+1)
        reverse(i+1,len(nums))
nums=[1,3,2]
Solution().nextPermutation(nums)
print(nums)
