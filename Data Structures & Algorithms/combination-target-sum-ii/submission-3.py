class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #duplicates possible
        #only choose an element once
        #order does matter
        #candidates is non-empty
        #is there always an answer (ans)
        #backtracking
            #at each step, either include value in combinatiron or not
            #base case: index out of bounds or sum is greater than target
            #increase i at every step
            #n 2^n time complexity. (why is backtracking the most efficient)
        candidates.sort()
        res = []
        subset = []

        def backtrack(i, target):
            if target == 0 :
                res.append(subset.copy())
                return
            if target < 0 or i >= len(candidates):
                return
            
            subset.append(candidates[i])
            backtrack(i+1,target-candidates[i])

            subset.pop()
            j=i
            while j < len(candidates) and candidates[j] == candidates[i]:
                j+=1
            backtrack(j,target)

        backtrack(0, target)
        return res
