
def get_next(x):
    nums=list(map(int,list(str(x))))
    ans= sum(map(lambda x:x*x,nums))
    print(x,'->',ans)
    return ans
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        found=set([n])
        while(True):
            if n==1:
                return True
            n=get_next(n)
            if n in found:
                #print('found loop')
                return False
            found.add(n)
print(Solution().isHappy(90))

        