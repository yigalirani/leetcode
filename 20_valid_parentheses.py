class Solution(object):
    def isValid(self, s):
        head=[0]
        pairs={
            '{':'}',
            '[':']',
            '(':')'
        }
        def look_ahead():
            if head[0]>=len(s):
                return '.'
            return s[head[0]]
        def read_token():
            ans=look_ahead()
            if ans!='.':
                head[0]+=1
            return ans
            
        def parse(end):
            while(True):
                c=read_token()
                if c==end:
                    return
                if c not in '{[(':
                    raise ValueError("syntax error") 
                parse(pairs[c])
            c=read_token()
        try:
            parse('.')
            return True
        except ValueError as er:
            return False
def run(*test_cases):
  for case in test_cases:
    result=Solution().isValid(case)
    print(result,case)

run(
  "()",
  "[([])]",
  "(((((}}}"
)
