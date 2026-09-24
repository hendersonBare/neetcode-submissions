class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def traverseIsland(i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] == "0" or grid[i][j] == "x":
                return
            grid[i][j] = "x"
            traverseIsland(i+1,j)
            traverseIsland(i-1,j)
            traverseIsland(i,j+1)
            traverseIsland(i,j-1)
            return
        
        
        num_islands = 0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == "1":
                    num_islands += 1
                    traverseIsland(i,j)
    
        return num_islands
    
        
