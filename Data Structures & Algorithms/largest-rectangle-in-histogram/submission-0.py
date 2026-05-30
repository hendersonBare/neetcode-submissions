class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            height = heights[i]
            width = 1
            l = r = i
            while l > 0:
                l -=1 
                if heights[l] >= height:
                    width += 1
                else:
                    break
            while r < len(heights)-1:
                r+=1
                if heights[r] >= height:
                    width += 1
                else:
                    break
            area = width * height
            max_area = max(area, max_area)
        return max_area