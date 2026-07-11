class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set()
        longest = 0
        for x in nums:
            seq.add(x)
        for x in nums:
            if x-1 not in seq:
                curr = x
                length = 0
                while curr in seq:
                    length += 1
                    curr += 1
                longest = max(length, longest)
        return longest
