class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        res = r
        while(l <= r):
            rate = (l + r) // 2

            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(float(piles[i]) / rate)
            if hours <= h: #rate needs to be higher
                res = rate
                r = rate - 1
            else:   #rate needs to be lower, also check if min
                l = rate + 1
        return res