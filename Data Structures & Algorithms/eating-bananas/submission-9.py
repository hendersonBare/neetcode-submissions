class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_rate = max(piles)

        def time_to_eat(rate: int):
            hours = 0
            for x in piles:
                hours += -(-x//rate)
            return hours

        a = 1
        b = max_rate

        min_rate = max_rate
        while a <= b:
            mid = (a + b) // 2
            time = time_to_eat(mid)
            if time <= h:
                min_rate = min(min_rate,mid)
                b = mid-1
            else:
                a=mid+1
        return min_rate

