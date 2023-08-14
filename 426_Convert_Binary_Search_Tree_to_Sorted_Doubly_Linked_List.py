# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root):
        def f(node):
            if node is None: return None
            left=f(node.left)
            right=f(node.right)
            if left is None and right is None:
                return Node(None,node,node)
            if right is None:
                node.left=left.right
                node.left.right=node
                return Node(None,left.right,node)
            if left is None:
                node.right=left.right
                node.left.right=node
                return Node(None,node,right.left)
            node.left=left.right
            node.right=right.left
            node.left.right=node            
            node.right.left=node        
            return Node(None,left,right)
        ans=f(root)
        ans.right.right=ans.left
        ans.left.left=ans.right
        return ans.left
    

from viztree import *
def main():
    t=deserialize('[2,1,3]')
    drawtree(t)
    ans=Solution().treeToDoublyList(t)   
    drawtree(ans)
main()