
from typing import List
import functools
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        line=1
        @functools.lru_cache(100000000)
        def f(pos,amount):

            def ret(ans):
                return ans
                nonlocal line
                line+=1
                #return ans
                first='eceeds'
                if pos<n:
                    first=coins[pos]
                print(line,': pos',pos,'first',first,'amount',amount,'ans',ans)
                return ans
            if amount==0 :
                return ret(0)
            if amount<0 or pos>=n:
                return ret(-1)
            first=coins[pos]
            if pos==n-1:
                if amount%first==0:
                    return amount//first
                return -1

            ans=9999999
            for x in range(amount//first+1):
                leftover=amount-first*x
                rest_ans=f(pos+1,leftover)
                if rest_ans!=-1:
                    ans=min(ans,x+rest_ans)
            if ans==9999999:
                return ret(-1)
            return ret(ans)
        coins=sorted(coins,reverse=True)
        n=len(coins)
        print('coins',coins)
        return f(0,amount)
def main():
    #print(Solution().coinChange([1,2,5],11))
   

    print(Solution().coinChange([19,28,176,112,30,260,491,128,70,137,253],8539))
        
main()