from collections import deque


class Solution(object): # ai converted from c++ to python https://leetcode.com/problems/shortest-distance-from-all-buildings/submissions/1603000087/
    def shortestDistance(self,grid):
        m, n = len(grid), len(grid[0])
        total = [row[:] for row in grid]  # Deep copy
        walk = 0
        delta = [0, 1, 0, -1, 0]
        count=0
        for i in range(m):
            for j in range(n):
                cell= grid[i][j]                
                if cell !=1:
                    continue
                mindist = -1
                dist = [row[:] for row in grid]
                q = deque()
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        ni, nj = x + delta[d], y + delta[d + 1]
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == walk:
                            count+=1
                            grid[ni][nj] -= 1
                            dist[ni][nj] = dist[x][y] + 1
                            total[ni][nj] += dist[ni][nj] - 1
                            q.append((ni, nj))
                            if mindist < 0 or mindist > total[ni][nj]:
                                mindist = total[ni][nj]
                walk -= 1
        print('count:',count)
        return mindist if mindist != -1 else -1
grid=[[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

ans=Solution().shortestDistance(grid)
print(ans)