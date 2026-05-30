class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        queue = deque()
        visited = {}
        num_islands = 0
        for i in range(0, row):
            for j in range(0, col):
                if grid[i][j] == "1" and (i,j) not in visited:
                    num_islands += 1
                    visited[(i,j)] = True
                    queue.extend([(i+1,j),(i-1,j),(i,j+1),(i,j-1)])
                    while (len(queue) > 0):
                        coord = queue.pop()
                        if (coord[0] < 0 or coord[0] >= row or 
                        coord[1] < 0 or coord[1] >= col or 
                        grid[coord[0]][coord[1]] == "0" or coord in visited):
                            continue
                        else:
                            visited[(coord)] = True
                            a, b = coord[0], coord[1]
                            queue.extend([(a+1,b),(a-1,b),(a,b+1),(a,b-1)])
        return num_islands
