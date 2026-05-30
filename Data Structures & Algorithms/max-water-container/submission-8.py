class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        max = 0
        while(l < r):
            min_bar = min(heights[l], heights[r])
            amt = (r-l) * (min_bar)
            if amt > max:
                max = amt
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max


