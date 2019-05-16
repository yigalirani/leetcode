from functools import lru_cache
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        words=set(wordDict)
        if len(words)==0:
            return []
        max_len=max([len(x) for x in words])
        @lru_cache(100000)
        def calc(start):
            print(start)
            ans=[]
            for i in range(start+1,len(s)+1):
                if i-start>max_len:
                    return ans
                start_word=s[start:i]
                if start_word in words:
                    if i==len(s):
                        ans.append([start_word])
                    for rest in calc(i):
                        ans.append([start_word]+rest)
            return ans
        for x in calc(0):
            print(' '.join(x))
        return [' '.join(x) for x in calc(0)]
ans=Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
print(ans)