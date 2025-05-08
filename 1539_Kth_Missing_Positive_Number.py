from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        last=0
        for x in arr:
            num_missing=x-last-1
            if num_missing>=k:
                return last+k
            last=x
            k-=num_missing
        return last+k
ans=Solution().findKthPositive([2,3,4,7,11],5)
print(ans)