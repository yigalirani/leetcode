def predict_it(nums):
    cache={}
    def cached(func):
        def caller(*args):
            key=','.join(map(str,args))
            if key in cache:
                return cache[key]
            value=func(*args)
            cache[key]=value
            return value
        return caller    
    @cached
    def play(left,right,player):
        if right-left==0:
            return nums[left]*player
        r=(
            play(left+1,right,player*-1)+nums[left]*player,
            play(left,right-1,player*-1)+nums[right]*player
        )
        if (player==1):
            return max(r)
        else:
            return min(r)
    ans=play(0,len(nums)-1,1)>=0
    #print cache 
    return ans

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return predict_it(nums)