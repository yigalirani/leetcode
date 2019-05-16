import viztree
class Solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

    def isCompleteTree(self,TreeNode):
        def f(r):
            if r is None:
                return 0,0,1
            children=[f(x) for x in [r.left,r.right] if x]
            if not (children):
                return 1,1,1
            if r.right and not r.left:
                return 0,0,0
            ans=(
                max([x[0] for x in children])+1,
                min([x[1] for x in children])+1,
                min([x[2] for x in children])
            )
            return ans
        the_max,the_min,ans=f(root)
        print(the_max,the_min,ans)
        return the_max-the_min<=1 and ans==1
                            
                    
root=viztree.deserialize('[1,2,3,5,null,7,8]')
viztree.drawtree(root)
            
        