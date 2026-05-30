class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [0] * len(nums)
        for i in range(0, len(nums)):
            value = 1
            for j in range(0, len(nums)):
                if (i == j):
                    continue
                else:
                    value *= nums[j]
            ret[i] = value
        return ret