class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #grid is non-empty
        #if no fresh fruits, return 0
        #use a multi-modal bfs where we add all rotten fruit to a queue
        #while the queue is non-empty, iterate over all, adding their neighbors
        #if they are fresh fruit
        #have a distance variable that increments by 1 after each iteration
        #once queue is empty, if no fresh fruit remain return distance
        #other wise, return -1

        num_fresh = 0
        q = deque()
        marked = set()

        def in_bounds(i,j):
            return (i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]))

        def find_neighbors(i,j):
            neighbors = [(-1,0),(1,0),(0,1),(0,-1)]
            for x,y in neighbors:
                a,b = i+x,j+y
                if in_bounds(a,b) and (a,b) not in marked and grid[a][b] == 1:
                    marked.add((a,b))
                    q.append((a,b))
            return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                    num_fresh += 1
                    marked.add((i,j))
                elif grid[i][j] == 1:
                    num_fresh +=1

        dist = -1
        while q:
            for i in range(len(q)):
                i,j = q.popleft()
                grid[i][j] = 2
                num_fresh -= 1
                find_neighbors(i,j)
            dist += 1
        if num_fresh == 0:
            if dist == -1:
                return 0
            else:
                return dist
        return -1
        
