def sign(x):
    if x>0:
        return 1
    return -2
class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        head=0
        n=len(nums)
        if n==0:
            return False
        def get_next(head):
            return (head+nums[head])%n
        print '->',head
        for i in xrange(n):
            head=get_next(head)
            print head
        if head==get_next(head):
            return False
        orig_sign=sign(nums[head])
        head2=head
        for i in xrange(n):
            head2=get_next(head2)
            if sign(nums[head2])!=orig_sign:
                return False
            if head2==head:
                return True
print Solution().circularArrayLoop( [3,1,2])