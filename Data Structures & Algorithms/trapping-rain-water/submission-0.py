class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = 0
        max_right = 0
        l_arr = [0] * len(height)
        r_arr = [0] * len(height)
        min_bars = []
        for i in range(len(height)):
            l_arr[i] = max_left
            max_left = max(max_left, height[i])

        for i in range(len(height)-1, -1, -1):
            r_arr[i] = max_right
            max_right = max(max_right, height[i])

        ret = 0
        for i in range(len(height)):
            ret += max(min(r_arr[i], l_arr[i]) - height[i], 0)

        return ret