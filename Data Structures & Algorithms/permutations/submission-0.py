class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        perm = []

        def dfs(nums): 
            if len(nums) == 0:
                ret.append(perm.copy())
                return
            for i in range(len(nums)):
                perm.append(nums[i])
                dfs(nums[:i] + nums[i+1:])
                perm.pop()
        dfs(nums)
        return ret