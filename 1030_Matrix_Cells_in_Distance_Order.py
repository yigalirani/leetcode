class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        cells=[]
        for row in range(rows):
            for col in range(cols):
                cells.append([row,col])
        return sorted(cells,key=lambda cell: abs(rCenter-cell[0])+abs(cCenter-cell[1]))

print(Solution().allCellsDistOrder(2,3,0,0))