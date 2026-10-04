class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #grid is never empty
        #possible to have no or all treasure chests
        #iterate over all squares in the grid
        #populate a queue with all of the treasure locations
        #run BFS from the treasure locations to calculate the distance
        #from each square to the treasure
        #make sure to mark the cells as we add them to the queue 
        #to handle potential duplicates
        #O(m*n) time complexity
        #O(m*n) space complexity
        q = deque()
        visit = set()
        
        def inBounds(x,y):
            return (x >= 0 and x < len(grid) and y>=0 and y < len(grid[0]))

        def addNeighbors(x,y):
            neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
            for a,b in neighbors:
                if (a,b) not in visit and inBounds(a,b) and grid[a][b] != -1:
                    visit.add((a,b))
                    q.append((a,b))


        def findIslands():
            dist=0
            while q:
                for i in range(len(q)):
                    x,y = q.popleft()
                    grid[x][y] = dist
                    addNeighbors(x,y)
                dist += 1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0 and (r,c) not in visit:
                    visit.add((r,c))
                    q.append((r,c))

        findIslands()

        return