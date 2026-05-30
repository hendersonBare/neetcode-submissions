class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0
        for x in nums:
            curr = max(rob2, x+rob1)
            rob1 = rob2
            rob2 = curr
        return rob2