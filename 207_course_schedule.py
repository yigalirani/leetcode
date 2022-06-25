#yigal: i did not invent this algorithm, i just wrote it from memory after reading, few days aga, someone elses solution
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses, prerequisites):
        g=defaultdict(set)
        for c,p in prerequisites:
            g[c].add(p)
        #print(g)
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
print (Solution().canFinish(2, [[1,0]]))
