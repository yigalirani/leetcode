# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import itertools 
def vcomb(v):
    return [x for l in range(0, len(v)+1) for x in itertools.combinations(v, l)]
def f(r):
    if r is None: return None
    children=[f(x) for x in [r.left,r.right] if x]
    snakes=[x[0] for x in children]
    birds=[x[1] for x in children]
    new_snake=max(snakes + [0])+r.val
    new_bird=max(map(sum,vcomb(snakes)) or [0])+r.val
    new_bird=max(birds+[new_bird])
    print(r.val,new_snake,new_bird)
    return new_snake,new_bird

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return f(root)[1]
def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root
def main():
    tree=deserialize('[-1,5,null,4,null,null,2,-4]')
    drawtree(tree_)
    print(Solution().maxPathSum(tree))
main()