class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = nums.copy()
        suffix = nums.copy()
        for i in range(1,len(nums)): #prefix
            prefix[i] *= prefix[i-1]
        for i in range (len(nums)-2,-1,-1): #suffix
            suffix[i] *= suffix[i+1]

        result = [1] * len(nums)
        for i in range(len(nums)):
            if not i-1<0:
                result[i]*= prefix[i-1]
            if not i+1>len(nums)-1:
                result[i]*= suffix[i+1]

        return result
