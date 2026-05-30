class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[j] == -1:
                return j
            else:
                temp = nums[j]
                nums[j] = -1
                j = temp
        return j