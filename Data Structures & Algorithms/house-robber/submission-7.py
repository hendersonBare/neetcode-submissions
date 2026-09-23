class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        mem = [0] * len(nums)
        mem[-1] = nums[-1]
        mem[-2] = max(nums[-2],mem[-1])

        for i in range(len(nums)-3,-1,-1):
            mem[i] = max(nums[i]+mem[i+2],mem[i+1])

        return mem[0]