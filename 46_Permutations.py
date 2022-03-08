def f(nums):
    if len(nums)==1:
        yield nums
    if len(nums)<=1:
        return
    for perm in f(nums[1:]):
        print(perm)
        for i in range(len(nums)+1):
            x= perm[:i]+nums[0:1]+perm[i:]
            print('yield',i,x)
            yield x
        
        
    
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(f(nums))
print(Solution().permute([1,2,3]))