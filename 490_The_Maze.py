def add (tuple1, tuple2):
    return tuple(a + b for a, b in zip(tuple1, tuple2))
def print_maze(maze,visited):
  for i,row in enumerate(maze):
      for j, col in enumerate(row):
          p=col
          if (i,j) in visited:
              p='*'
          print(p,'',end='')
      print('')    
class Solution:
    def hasPath(self, maze, start, destination):
        m=len(maze)
        n=len(maze[0])
        print(m,n)
        def bump(start,diff):
            while True:
                new_point=add(start,diff)
                row,col=new_point
                if row<0 or col<0 or row>=m or col>=n :
                    return start
                if maze[row][col]!=0:
                    return start
                start=new_point
        visited=set()
        def visit(row,col):
            if (row,col) in visited:
                return
            visited.add((row,col))
            for dir in [(0,1),(0,-1),(1,0),(-1,0)]:
                new_pos=bump((row,col),dir)
                visit(*new_pos)
        visit(*start)
        print(visited)
        print_maze(maze,visited)
        return tuple(destination) in visited
maze=[[0,0,1,0,0],
      [0,0,0,0,0],
      [0,0,0,1,0],
      [1,1,0,1,1],
      [0,0,0,0,0]]

    
print(Solution().hasPath(maze,[0,4],[4,4]))