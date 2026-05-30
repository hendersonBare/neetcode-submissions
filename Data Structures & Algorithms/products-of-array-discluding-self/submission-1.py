class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1] * len(nums)
        value = 1
        for i in range(0, len(nums)):
            ret[i] *= value
            value *= nums[i]
        value = 1
        for i in range(len(nums)-1,-1,-1):
            ret[i] *= value
            value *= nums[i]
        return ret