class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        fleets = []
        for pos, speed in sorted(cars)[::-1]:
            diff = (target-pos)/speed
            fleets.append(diff)
            if len(fleets)>1 and fleets[-1]<=fleets[-2]:
                fleets.pop()
        return len(fleets)

