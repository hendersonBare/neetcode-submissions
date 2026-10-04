class Solution:
    def rob(self, nums: List[int]) -> int:
        #nums is non empty
        #each num is non-negative
        #dynamic programming problem
        #base case: no houses to rob
        #choices: at each house we can either rob or skip
        #make sure that the memoization values are out of range or
        memo = [-1] * len(nums)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            memo[i] = max(nums[i] + memo[i-2], memo[i-1])
        return memo[-1]

