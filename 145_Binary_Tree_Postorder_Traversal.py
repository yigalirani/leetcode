# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def post_order(tree):
    if tree is None:
        return
    for x in post_order(tree.left):
        yield x
    for x in post_order(tree.right):
        yield x    
    yield tree.val

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return list(post_order(root))