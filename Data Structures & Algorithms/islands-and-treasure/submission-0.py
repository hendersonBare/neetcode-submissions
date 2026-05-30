class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append([i,j])
                    visit.add((i,j))

        def addRoom(i,j):
            if (min(i,j) < 0 or i > rows-1 or j > cols-1 or
                grid[i][j] == -1 or (i,j) in visit):
                return
            visit.add((i,j))
            q.append([i,j])
            

        dist = 0
        while q:
            for i in range(len(q)):
                i,j = q.popleft()
                grid[i][j] = dist

                addRoom(i+1,j)
                addRoom(i-1,j)
                addRoom(i,j+1)
                addRoom(i,j-1)

            dist += 1