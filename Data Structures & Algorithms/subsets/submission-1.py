class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                ret.append(subset.copy())
                return
            #we need the case where we do include this value
            subset.append(nums[i])
            dfs(i+1)
            #the case where we don't include this value
            subset.pop()
            dfs(i+1)

        dfs(0)
        return ret