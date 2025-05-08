
class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        path={}
        ans=set()
        def build_path(node):
            if node==None:
                return -1
            if node==target:
                print('at target')
                path[node.val]={'node':node,'dist':0}
                return 0
            
            for  child in filter(None,[node.left,node.right]):
                dist=build_path(child)
                if dist!=-1:
                  path[node.val]={'node':node,'dist':dist+1}
                  return dist+1
            return -1
        build_path(root)
        print(path)
        def f(node,k):
            if (k==0):
                ans.add(node.val)
                return
            for child in filter(None,[node.left,node.right]):   
                if path.get(child.val)==None:
                    f(child,k-1)
            
        values=list(path.values())
        print('values',values)
        for x in values:
            f(x['node'],k-x['dist'])
        return list(ans)     
def find_target(node,target):
    if node==None:
        return None
    if node.val==target:
        return node
    return find_target(node.left,target) or find_target(node.right,target)
from viztree import deserialize,drawtree
root=deserialize('[3,5,1,6,2,0,8,null,null,7,4]')
target=find_target(root,5)
#drawtree(root)
ans=Solution().distanceK(root,target,2)    
print('ans',ans)  
