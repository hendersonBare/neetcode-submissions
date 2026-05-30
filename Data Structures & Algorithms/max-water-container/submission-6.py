class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        for i in range(len(heights)):
            min_bar = heights[i]
            for j in range(i+1, len(heights)):
                min_bar = heights[i]
                other_bars = 0
                if heights[j] < heights[i]:
                    min_bar = heights[j]
                amt = ((j - i) * min_bar)
                print(i,j,amt, min_bar)
                if amt > max:
                    max = amt
        return max

