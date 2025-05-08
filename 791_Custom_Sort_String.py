from collections import defaultdict
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count=defaultdict(int)
        ans=[]
        inorder=set()
        for c in s:
            count[c]+=1
        for c in order:
            inorder.add(c)
            ans.append(c*count[c])
        for c in s:
            if  c not in inorder:
                ans.append(c)
        return ''.join(ans)

        