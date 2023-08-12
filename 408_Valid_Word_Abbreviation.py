import re
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if re.match('^0|[a-z]0',abbr):
            return False
        head=0
        for x in re.findall('[1-9][0-9]*|[a-z]+',abbr):
            try:
              head+=int(x)
            except ValueError:
              if word[head:head+len(x)]!=x:
                 return False
              head+=len(x)
        return head==len(word)

print(Solution().validWordAbbreviation("a","2"))