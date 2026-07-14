class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most = 0
        i = 0
        j = len(heights)-1
        while i < j:
            water = min(heights[i],heights[j])*(j-i)
            most = max(most, water)
            if heights[i] < heights[j]:
                i+=1
            elif heights[i] > heights[j]:
                j-=1
            else:
                if heights[i+1]>heights[j-1]:
                    i+=1
                else:
                    j-=1
        return most