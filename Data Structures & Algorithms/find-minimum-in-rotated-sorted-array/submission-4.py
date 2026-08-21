class Solution:
    def findMin(self, nums: List[int]) -> int:
        num_rotations = 0
        l = 0
        r = len(nums)-2
        #first find the number of rotations
        #return the value that is one after the number of rotations
        #since that is the min number
        while l <= r:
            m = (l + r) // 2
            if nums[m+1] < nums[m]:
                return nums[m+1]
            if nums[m+1] > nums[m] and nums[m+1] < nums[l]:
                r = m-1
            else:
                l = m+1
        return nums[0]


