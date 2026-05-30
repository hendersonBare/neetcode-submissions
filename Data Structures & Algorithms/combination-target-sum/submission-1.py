class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        path = []
        def explore_combination(i, target):
            if target == 0:
                ret.append(path.copy())
                return
            if i >= len(nums) or target < 0:
                return
            
            path.append(nums[i])
            explore_combination(i, target-nums[i])
            path.pop()
            explore_combination(i+1, target)
        explore_combination(0, target)
        return ret