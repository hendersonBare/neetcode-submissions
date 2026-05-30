class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        num_fleets = 0
        tup = [list(pair) for pair in zip(position,speed)]
        sorted_tup = sorted(tup, key=lambda x:x[0])
        res = []
        for i in range(len(sorted_tup)-1,-1,-1):
            fleet = ((target-sorted_tup[i][0])/sorted_tup[i][1])
            if (len(res)==0 or fleet > res[-1]):
                res.append(fleet)
        return len(res)