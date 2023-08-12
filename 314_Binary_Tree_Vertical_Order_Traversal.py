
from viztree import deserialize,drawtree
import collections
class Solution(object):
    def verticalOrder(self, root):
        depth=0
        h=collections.defaultdict(list)
        q=[(root,0)]
        for node,pos in q:
            if node:
                h[pos].append(node.val)
                q+=[(node.left,pos-1)]
                q+=[(node.right,pos+1)]
                depth=max(depth,abs(pos+1),abs(pos-1))
            
        ans=[]
        for i in range(-depth,depth+1):
            x=h.get(i,None)
            if x:
                ans.append(x)
        return ans
        


def test(stree):
  tree=deserialize(stree)
  ans=Solution().verticalOrder(tree)
  print(ans)
  drawtree(tree)


test('[3,9,20,null,null,15,7]')
