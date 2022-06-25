from collections import defaultdict
def canFinish(numCourses: int, g):

    h={}
    def has_circle(node):
        if h.get(node)==-1: #mrans proccessing
            return True
        if h.get(node)==0:
            return False
        h[node]=-1
        for nei in g[node]:
            if has_circle(nei):
                return True
        h[node]=0
        return False

    for i in range(numCourses):
        if has_circle(i):
            return False
    return True
class Solution:
    def findOrder(self, numCourses, prerequisites):
        g=defaultdict(set)
        for c,p in prerequisites:
            g[c].add(p)        
        if not canFinish(numCourses, g):
            return []
        ans=[]
        dumped=set()
        def dump(node):
            if node in dumped:
                return
            for i in g[node]:
                dump(i)
            ans.append(node)
            dumped.add(node)
        for i in range(numCourses):
            dump(i)
        return ans
print(Solution().findOrder(2, [[1,0]]))