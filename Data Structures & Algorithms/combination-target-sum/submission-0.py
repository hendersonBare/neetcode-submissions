class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        paths = {}
        path = []
        def explore_combination(nums, target):
            if target == 0:
                print(path)
                spath = sorted(path)
                print(spath)
                if tuple(spath) not in paths:
                    ret.append(spath)
                    paths[tuple(spath)] = 1
                return
            elif target < 0:
                return
            for x in nums:
                path.append(x)
                explore_combination(nums, target-x)
                path.pop()
        explore_combination(nums, target)
        return ret