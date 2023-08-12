import functools 
class Solution:
    @functools.lru_cache(1000)
    def isOneEditDistance(self, s: str, t: str) -> bool:
        def f(s,t,dist):
            if (dist==0):
                return s==t
            if (s==t):
                return False
            dist2=1 if s[:1]==t[:1] else 0
            return f(s[1:],t,0) or \
                   f(s,t[1:],0) or \
                   f(s[1:],t[1:],dist2)
        return f(t,s,1)
print(Solution().isOneEditDistance("ab","acb"))