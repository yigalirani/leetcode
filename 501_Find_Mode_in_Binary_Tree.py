# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
def get_vals(root):
    if root is None:
        return
    yield root.val
    for x in get_vals(root.left): yield x
    for x in get_vals(root.right): yield x    
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        c=defaultdict(int)
        for x in get_vals(root):
            c[x]+=1
        tops=sorted(c.iteritems(),key=lambda tup: tup[1],reverse=True)
        top_val=tops[0][1]
        #print tops,top_val
        return [name for name,value in tops if value==top_val]