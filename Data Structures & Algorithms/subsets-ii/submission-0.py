class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ret = []
        path = []

        def dfs(i):
            if i >= len(nums):
                ret.append(path.copy())
                return
            
            path.append(nums[i])
            i+=1
            dfs(i)
            path.pop()
            while i < len(nums) and nums[i] == nums[i-1]:
                i+=1
            dfs(i)
        dfs(0)
        return ret
