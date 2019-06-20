from viztree import *
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def f(root,add):
            if root is None:
                return 0
            new_add=add*2+root.val
            if root.left is None and root.right is None:
                return new_add
 
            return f(root.left,new_add)+f(root.right,new_add)
        return f(root,0)
t=deserialize("[1,1,1]")
print(Solution().sumRootToLeaf(t))
drawtree(t)
        
