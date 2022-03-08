def prt(*argv):
  pass
class Solution:
    def change(self, amount, coins):
        def f(amount,start,indent):
            prt('   '*indent,amount,start)
            if amount<0:
                prt('   '*indent,'return 0')
                return 0
            if amount==0:
                prt('   '*indent,'return 1')
                return 1
            if start==len(coins):
                prt('   '*indent,'return 0 no more cons')
                return 0
            coin=coins[start]
            ans=0
            prt('   '*indent,'coin=',coin)
            for used in range(0,amount+1,coin):
                ans+=f(amount-used,start+1,indent+1)
            prt('   '*indent,'return',ans)    
            return ans
        return f(amount,0,0)

class Solution2:
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for amt in range(1, amount + 1):
               if amt >= coin:
                   dp[amt] += dp[amt - coin]
        return dp[amount]

print(Solution().change(100,[1,2,4,3,6,5]))
print(Solution2().change(100,[1,2,4,3,6,5]))