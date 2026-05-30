class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        max_length = 0
        curr_length = 1
        last = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == last + 1:
                curr_length += 1
                last = nums[i]
            elif nums[i] == last:
                continue
            else:
                last = nums[i]
                curr_length = 1
            if curr_length > max_length:
                max_length = curr_length
        if curr_length > max_length:
            max_length = curr_length
        return max_length
