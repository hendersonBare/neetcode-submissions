class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # to start we will write a loop that visits every node,
        # if the loop is unvisited then we will call a recursive helper 
        # method that visits all neighbors and increments the value.
        # we will create a map where the root of the 'island' correspinds 
        # to the area, we will then select the max area of the map
        area_dict = {}
        visited = {}

        def find_max_area(i,j):
            if (i < 0 or i >= len(grid) or j < 0 
            or j>= len(grid[0]) or (i,j) in visited or grid[i][j] == 0):
                return 0
            visited[(i,j)] = True
            return (grid[i][j] + find_max_area(i+1,j) + find_max_area(i-1,j) +
            find_max_area(i,j+1) + find_max_area(i,j-1))
            


        for i in range(len(grid)):
            for j in range(len(grid[0])): #assume sqaure grid
                if (i,j) not in visited:
                    area_dict[(i,j)] = find_max_area(i,j)

        return max(area_dict.values())

        