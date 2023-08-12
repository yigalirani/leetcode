import re

class Tokenizer:
  def __init__(self,s):
      self.head=0
      self.tokens=re.findall('\d+|\+|\-|\/|\*',s)
      self.n=len(self.tokens)
  def lookahead(self):
    if self.head>=self.n:
        return None
    return self.tokens[self.head]
  def read_token(self):
      ans=self.lookahead()
      self.head+=1 #todo: conditiaonal
      return ans
mult_funcs={
    '*':lambda x,y:x*y,
    '/':lambda x,y:x/y
}
add_funcs={
    '+':lambda x,y:x+y,
    '-':lambda x,y:x-y
}

class Solution:
    def calculate(self, s: str) -> int:
        tokenizer=Tokenizer(s)
        def read_mult():
            operand=tokenizer.read_token()
            if operand is None:
                return None
            ans=int(operand) #todo: error if not int
            operator=tokenizer.lookahead()
            func=mult_funcs.get(operator)
            if func is None:
                return ans
            tokenizer.read_token()
            operand=read_mult()
            return func(ans,operand)
        def read_add():
            ans=read_mult()
            if ans is None:
               return None
            operator=tokenizer.lookahead()
            func=add_funcs.get(operator)
            if func is None:
                return ans
            tokenizer.read_token()
            operand=read_add()
            return func(ans,operand)
        return read_add()

print(Solution().calculate('1+1+1'))