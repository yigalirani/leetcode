from collections import defaultdict
class Solution:
    def largestIsland(self, grid):
        for row in grid:
          print(row)      
        cur_island=2
        m=len(grid)
        n=len(grid[0])
        def iter_nei(i,j):
            for di,dj in [(-1,0),(+1,0),(0,-1),(0,+1)]:
                if 0<=i+di<m and 0<=j+dj<n:
                    yield i+di,j+dj
        def mark(i,j):
            if grid[i][j]!=1:
                return
            grid[i][j]=cur_island
            for i2,j2 in iter_nei(i,j):
                mark(i2,j2)
        for i in range(m):
            for j in range(n):
                mark(i,j)
                cur_island+=1
        islands=defaultdict(int)
        for i in range(m):
            for j in range(n):
                islands[grid[i][j]]+=1
            
        ans=0
        islands[0]=0
        for i in range(m):
            for j in range(n):
              if grid[i][j]!=0:
                continue
              nei_islands=set()
              for i2,j2 in iter_nei(i,j):
                  nei_islands.add(grid[i2][j2])
              lens=[islands[island] for island in nei_islands]
              cur=sum(lens)
              ans=max(ans,cur)
        return max(ans+1,max(islands.values()))
ans=Solution().largestIsland(
[[0,0,0,0,0,0,0],[0,1,1,1,1,0,0],[0,1,0,0,1,0,0],[1,0,1,0,1,0,0],[0,1,0,0,1,0,0],[0,1,0,0,1,0,0],[0,1,1,1,1,0,0]])
print(ans)          

        
                
            