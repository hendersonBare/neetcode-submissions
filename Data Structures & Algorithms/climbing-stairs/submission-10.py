class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 0
        curr = 0
        for i in range(n):
            curr = first + second
            temp = first
            first = curr
            second = temp
        return curr