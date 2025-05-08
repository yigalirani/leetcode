import re
class Solution:
    def calculate(self, s: str) -> int:
        tokens=re.findall('\d+|\+|\-|\/|\*|\(|\)|\$',s+'$')
        #for token in tokens:print(token)
        head=-1
        lookahead=None
        def read_token():
            nonlocal head,lookahead
            head+=1
            ans=lookahead
            lookahead=tokens[head]
            return ans
        read_token()
        def read_parntasys():
            if lookahead=='(':
                read_token()
                ans=read_add_minus()
                read_token() #todo: verify that )
                return ans
            if lookahead=='-':            
                read_token()
                return -read_parntasys()
            if lookahead.isnumeric():
                return int(read_token())
            #todo throw error here
        def read_term():            
            ans=read_parntasys()
            while True:
              match lookahead:
                  case '*':
                      read_token()
                      ans=ans*read_parntasys()
                  case '/':
                      read_token()
                      ans=ans//read_parntasys()                
                  case _:
                      return ans
              
        def read_add_minus():
            ans=read_term()
            while True:
                match lookahead:
                    case '+':
                        read_token()
                        ans+=read_term()
                    case '-':
                        read_token()
                        ans-=read_term()
                    case _:
                        return ans
        return read_add_minus()


print(Solution().calculate("2*3*4"))
print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))
print(Solution().calculate("- (3 + (4 + 5))"))
print(Solution().calculate("1-(     -2)"))
