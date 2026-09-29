class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #template:
        #1 base case
        #   the current number = target, or target is 0
        #   the index is out of bounds
        #2 constraints
        #   no duplicate combinations
        #   all elements of nums are distinct
        #   target is at least 2
        #3 choice 
        #   we can either subtract the number from target or
        #   not and move on
        #4 the backtracking step
        res = []
        comb = []
        def sum(i,target):
            if i >= len(nums) or target < 0:
                return
            elif target==0:
                res.append(comb.copy())
                return
            else:
                #choose num
                comb.append(nums[i])
                sum(i,target-nums[i])

                comb.pop()
                sum(i+1,target)
            return
        
        sum(0,target)
        return res

