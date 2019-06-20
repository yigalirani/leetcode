class Solution:
    def findTargetSumWays(self, nums, S):
        def f(start,S):
            v=nums[start:]
            if len(v)==0:
                return 0
            if len(v)==1:
                return int(v[0]==S)+int(v[0]==-S)
            return f2(start+1,S-v[0])+f2(start+1,S+v[0])
        h={}
        def f2(start,S):
            
            ans=h.get((start,S))
            if ans is not None:
                return ans
            ans=f(start,S)
            #print(S,nums,ans)
            h[(start,S)]=ans
            return ans
        nums=sorted(nums)
        return f2(0,S)
ans=Solution().findTargetSumWays([42,24,30,14,38,27,12,29,43,42,5,18,0,1,12,44,45,50,21,47],38)
print(ans)