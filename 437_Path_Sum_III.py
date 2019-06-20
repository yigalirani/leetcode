# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from viztree import *
from collections import Counter
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def f(root,sums):
            if root is None:
                return 0
            new_sum=Counter()
            ans=0
            for x,count in sums.items():
                if x==root.val:
                    ans+=count
                new_sum[x-root.val]+=count
            new_sum[sum]+=1
            return ans+f(root.left,new_sum)+f(root.right,new_sum)
        return f(root,Counter({sum:1}))
def main():
    t=deserialize('[1,0,1,1,2,0,-1,0,1,-1,0,-1,0,1,0]')
    drawtree(t)
    print(Solution().pathSum(t,2))
main()

            
