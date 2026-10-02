class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visit = set()
        def outOfBounds(r,c):
            return (r<0 or r>=len(grid) or c<0 or c>=len(grid[0]))

        def addNeighbors(r,c):
            neighbors = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for a,b in neighbors:
                if outOfBounds(a,b) or grid[a][b] == -1 or (a,b) in visit:
                    continue
                else:
                    visit.add((a,b))
                    q.append((a,b))
            return

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addNeighbors(r,c)

            dist += 1

        return