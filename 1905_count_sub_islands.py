class Solution:
    def countSubIslands(self, grid1,grid2):
        m=len(grid1)
        n=len(grid1[0])
        cur_island=2
        islands=set()
        non_islands=set()
        def mark(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid2[i][j]==0:
                return
            if grid2[i][j]>1:
                return False
            grid2[i][j]=cur_island
            islands.add(cur_island)
            if grid1[i][j]==0:
               non_islands.add(cur_island) 
            mark(i-1,j)
            mark(i+1,j)
            mark(i,j-1)
            mark(i,j+1)
        for i in range(m):
            for j in range(n):
                mark(i,j)
                cur_island+=1
        return len(islands)-len(non_islands)
ans=Solution().countSubIslands([[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],
[[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]])
print(ans)