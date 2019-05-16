class Tokenzier:
    def __init__(self,s):
        self.s=s
        self.head=0
    def read(self):
        ans=self.look()
        if ans is not None:
            self.head+=1
        return ans
    def look(self):
        if self.head==len(self.s):
            return None
        return self.s[self.head]

class Solution:  
    def removeOuterParentheses(self, S: str) -> str:
        t=Tokenzier(S)
        def read_prim():
            ans=[]
            if t.look()!='(':
                return ''
            ans.append(t.read())
            while True:
                if t.look()==')':
                    ans.append(t.read())
                    return ''.join(ans)
                prim=read_prim()
                if prim=='': #this is actualy syntax error
                    return ''.join(ans)
                ans.append(prim)

        ans=[]
        while True:
            prim=read_prim()
            if not prim:
                return ''.join(ans)
            ans.append(prim[1:-1])


print(Solution().removeOuterParentheses("(()())(())"))