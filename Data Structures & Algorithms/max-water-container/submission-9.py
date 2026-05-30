class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_amt = 0
        while l < r:
            max_amt = max(max_amt,(r - l) * min(heights[l], heights[r]))
            if heights[r] < heights[l]:
                r-=1
            else:
                l+=1
        return max_amt