import functools

        
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        @functools.lru_cache(1024)
        def calc(target):
            ans=set()
            if target<=0:
                return ans
            for i,x in enumerate(candidates):
                if x>target:
                    continue
                if x==target:
                    ans.add((x,))
                for y in calc(target-x):
                    ans.add(tuple(sorted((x,)+y)))
            return ans
    
        return list(calc(target))
ans=Solution().combinationSum([2,3,6,7],7)
print(ans)