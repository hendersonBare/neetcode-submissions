class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #subsequence is strictly increasing, so cannot be equal
        #nums is nonempty
        #nums can be negative
        #nums is unordered
        #subproblems will be the subsequences starting at later indices
        #we will iterate over nums backwards, and calculate the longest
        #possible subsequence starting at that index
        #a valid subproblem corresponds to a later index that has a higher value
        #after we populate the memo structure we will return a max of that
        LIS = [1] * len(nums)
        for i in range(len(nums),-1,-1):
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    LIS[i] = max(LIS[i],1+LIS[j])
        return max(LIS)