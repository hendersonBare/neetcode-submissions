class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {} # (r,c) -> value

        def DFS(r, c, prevVal):
            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or
                matrix[r][c] <= prevVal):
                return 0
            if ((r,c) in cache):
                return cache[(r,c)]
            
            length = 1
            length = max(length, 1 + DFS(r+1,c, matrix[r][c]))
            length = max(length, 1 + DFS(r-1,c, matrix[r][c]))
            length = max(length, 1 + DFS(r,c+1, matrix[r][c]))
            length = max(length, 1 + DFS(r,c-1, matrix[r][c]))

            cache[(r,c)] = length
            return length

        for i in range(0, ROWS):
            for j in range(0, COLS):
                DFS(i,j,-1)
        return max(cache.values())

