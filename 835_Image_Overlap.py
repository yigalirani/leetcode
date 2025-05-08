import collections
def make_scatter(A):
    N = len(A)
    ans=[]
    for i in range(N * N):
        row=i // N
        col=i % N
        if A[row][col]:
            ans.append(i // N * 100 + i % N)
    return ans
#    return [i // N * 100 + i % N for i in range(N * N) if A[i // N][i % N]]
class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        ## from https://leetcode.com/problems/image-overlap/solutions/130623/c-java-python-straight-forward/
        N = len(A)
        LA = make_scatter(A)
        LB = make_scatter(B)
        coun=[i - j for i in LA for j in LB]
        c = collections.Counter(coun)
        return max(c.values() or [0])
    
ans=Solution().largestOverlap([[1,1,0],[0,1,0],[0,1,0]],[[0,0,0],[0,1,1],[0,0,1]])
print(ans)