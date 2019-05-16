from viztree import *
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans=10000
        if root is None:
            return ans
        if root.left:
            ans=min(ans,abs(root.val-root.left.val),self.getMinimumDifference(root.left))
        if root.right:
            ans=min(ans,abs(root.val-root.right.val),self.getMinimumDifference(root.right))
        return ans
tree=deserialize('[236,104,701,null,227,null,911]')
drawtree(tree)
print(Solution().getMinimumDifference(tree))
        