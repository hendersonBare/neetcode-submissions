class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #constraints: 1's cannot be connected diagonally
        #grid len > 0, so no need to handle empty grids

        def outOfBounds(i,j):
            return (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]))

        #init a map for marking squares
        marked = {}
        #init a var for max area
        max_size = 0
        
        def dfs(i,j):
            if outOfBounds(i,j) or grid[i][j] == 0:
                return 0
            marked[(i,j)] = True
            size = 1
            neighbors = [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]
            for n in neighbors:
                if n not in marked:
                    size += dfs(n[0],n[1])
            return size


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in marked and grid[i][j] == 1:
                    max_size = max(dfs(i,j),max_size)
                

        return max_size

        

        

