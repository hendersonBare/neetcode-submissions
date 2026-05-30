class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedtuples = []
        for i in range(len(position)):
            sortedtuples.append((position[i], speed[i]))
        sortedtuples = sorted(sortedtuples, key=lambda x: x[0])

        stack = []

        for i in range(len(sortedtuples)-1, -1, -1):
            pos, speed = sortedtuples[i][0], sortedtuples[i][1]
            stack.append((target - pos) / speed)
            if (len(stack) > 1 and stack[-2] >= stack[-1]):
                stack.pop()

        return len(stack)
