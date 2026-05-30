class Solution:
    #isn't this just the same as fibonacci?
    def climbStairs(self, n: int) -> int:
        arr = [0] * (n+1)
        arr[0] = 1
        arr[1] = 1
        for i in range(2, len(arr)):
            arr[i] = arr[i-1] + arr[i-2]

        return arr[n]