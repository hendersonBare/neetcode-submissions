class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while(l < r):
            mid = (l + r) // 2
            print(mid)
            if mid > 0 and nums[mid-1] > nums[mid]:
                return nums[mid]
            elif nums[r] < nums[mid]:
                l = mid+1
            else:
                r = mid-1
        return nums[l]
