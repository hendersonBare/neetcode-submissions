class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #nums will always have atleast one value, will not be null
        #all integers will be unique
        #solution can be returned in any order
        #we will use a backtracking implementation to approach this problem
        #at each stage, we can either select the item and add it to a set or skip it
        #once we reach an out of bounds index, we can add the subset to our results
        #since we are working left to right and all numbers are unique, we should naturally not include any duplicates
        #since there are 2^n possible subsets to create with each num, overall time cmplexity will be O(n2^n)

        res = []
        subset = []
        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            backtrack(i+1)

            subset.pop()
            backtrack(i+1)

        backtrack(0)
        return res
