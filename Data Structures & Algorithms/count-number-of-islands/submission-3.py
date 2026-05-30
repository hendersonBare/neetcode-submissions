class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_num = len(grid)
        col_num = len(grid[0])
        num_islands = 0
        for i in range(row_num):
            for j in range(col_num):
                if (grid[i][j] == '1'):
                    num_islands += 1
                    self.isIsland(grid, i, j, row_num, col_num)
        return num_islands

    def isIsland(self, grid, i,j, row_num, col_num) -> bool:
        if (0 > i or i > row_num-1 or 0 > j or j > col_num-1):
            return True
        if grid[i][j] != '1':
            return True
        grid[i][j] = '2'
        return (self.isIsland(grid, i+1, j, row_num, col_num) and self.isIsland(grid, i-1, j, row_num, col_num) and
            self.isIsland(grid, i, j+1, row_num, col_num) and self.isIsland(grid, i, j-1, row_num, col_num))
        
