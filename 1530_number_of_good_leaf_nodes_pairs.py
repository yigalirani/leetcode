import collections
def inc(a):
    return {name+1:value for name,value in a.items()}
class Solution:
    def countPairs(self, root, distance):
        all_pairs=set()
        def cross_count(a,b):
            ans=0
            for dist,cnt in a.items():
                for target_dist in range(0,distance-dist-2+1):
                    match=b.get(target_dist,set())
                    for pair1 in cnt:
                        for pair2 in match:
                            all_pairs.add(tuple(sorted((pair1,pair2))))

                        
            return ans
        def merge(a,b):
            a=a.copy()
            for dist,vals in b.items():
                if dist in a:
                    a[dist]=a[dist].union(vals)
                else:
                    a[dist]=vals
            return a
                
        def f(node):
            if node is None:
                return {}
            if node.left is None and node.right is None: #leaf
                return {0:set([node.val])}
            left=f(node.left)
            right=f(node.right)
            cross_count(inc(left),inc(right))
            cross_count(right,left)
            ans=merge(inc(left),inc(right))
            return ans
        ans=f(root)
        print(all_pairs)
        return len(all_pairs)
from viztree import *

#root=deserialize('[1,2,3,null,4]')
root=deserialize('[1,2,3,4,5,6,7]')


drawtree(root)
print(Solution().countPairs(root,3))