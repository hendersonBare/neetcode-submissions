class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = {}
        num_islands = 0

        def exploreIsland(coord):
            a = coord[0]
            b = coord[1]
            if (a < 0 or a >= row or b < 0 or b >= col or 
            coord in visited or grid[a][b] == '0'):
                return
            else:
                visited[coord] = True
                exploreIsland((a+1,b))
                exploreIsland((a-1,b))
                exploreIsland((a,b+1))
                exploreIsland((a,b-1))
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and (i,j) not in visited:
                    exploreIsland((i,j))
                    visited[(i,j)] = True
                    num_islands += 1
                    

        return num_islands

       
