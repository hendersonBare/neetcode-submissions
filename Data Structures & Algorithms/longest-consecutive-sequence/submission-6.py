class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = {}
        start = []
        for x in nums:
            vals[x] = 0
        for x in nums:
            if x-1 not in vals:
                start.append(x)
        curr_length = 0
        max_length = 0
        for x in start:
            curr_length = 1
            last = x
            while ((last + 1) in vals):
                curr_length += 1
                last = last + 1
            if curr_length > max_length:
                max_length = curr_length
        return max_length