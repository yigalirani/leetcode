
# based on the algorithm in the soltion
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m=len(mat)
        n=len(mat[0])
        ans=[]
        is_reverse=False
        def do_loop(start_i,start_j):
            nonlocal is_reverse
            is_reverse=not is_reverse
            h=0
            local_ans=[]
            while True:
                i=start_i+h
                j=start_j-h
                if i>=m or j<0:
                    break
                h+=1
                local_ans.append(mat[i][j])
            if is_reverse:
                return ans.extend(reversed(local_ans))
            return ans.extend(local_ans)
                


        for j in range(0,n):
            do_loop(0,j)
        for i in range (1,m):
            do_loop(i,n-1)
        return ans

        