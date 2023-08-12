import re
class Solution:
    def calculate(self, s: str) -> int:
        tokens=re.findall('\d+|\+|\-|\/|\*|\$',s+'$')
        head=0
        def look_ahead():
          return tokens[head]
        def read_token():
          nonlocal head
          ans=look_ahead()
          head+=1
          return ans
        def read_term():
          ans=1
          sign='*'
          if look_ahead()=='$':
            return None             
          while True:
            c=read_token()
            num=int(c)
            if sign=='*':
              ans=ans*num
            else:
              ans=ans//num
            sign=look_ahead()
            if sign not in '*\/':
              return ans
            read_token()
            
        def read_expr():
          ans=0
          sign=1
          while True:
            term=read_term()
            if term is None:
              return ans
            ans+=sign*term
            c=read_token()
            if c=='$':
              return ans
            sign=1 if c=='+' else -1
        return read_expr()
print(Solution().calculate('10-2*8'))