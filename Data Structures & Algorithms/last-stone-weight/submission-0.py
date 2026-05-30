class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            print(stones)
            x = -1 * (heapq.heappop(stones))
            y = -1 * (heapq.heappop(stones))
            if x == y:
                continue
            elif x < y:
                heapq.heappush(stones, -1*(y-x))
            else:
                heapq.heappush(stones, -1*(x-y))
        if len(stones) == 0:
            return 0
        else:
            return -1*(heapq.heappop(stones))
