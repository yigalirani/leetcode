# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from viztree import TreeNode,drawtree
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.postorder=postorder
        self.inorder=inorder
        return self.build(len(postorder),0,0,0)
    def build(self,n,poststart,instart,level):
        #print '    '*level,'build',n,prestart,instart
        if (n==0):
            return None
        if (n==1):
            return TreeNode(self.postorder[poststart])
        node_val=self.postorder[poststart+n-1]
        ans=TreeNode(node_val)
        index= self.inorder.index(node_val)
        #index=self.inorder_index(self.preorder[prestart],instart,n)
        left_size=index-instart
        right_size=n-left_size-1
        #print '    '*level,'index=',index,'left_size=',left_size,'right_size=',right_size
        ans.left=self.build(left_size,poststart,instart,level+1)
        ans.right=self.build(right_size,poststart+left_size,instart+left_size+1,level+1)
        return ans
        
tree=Solution().buildTree([9,3,15,20,7], [9,15,7,20,3])
drawtree(tree)
        