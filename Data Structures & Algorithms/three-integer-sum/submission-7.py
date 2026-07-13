class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []
        triplet_set = set()

        def two_sum(i):
            if len(nums)-i<3:
                return
            j=i+1
            k=len(nums)-1
            target = -nums[i]
            while j < k:
                curr = nums[j]+nums[k]
                if curr==target:
                    triplet = [nums[i],nums[j],nums[k]]
                    if tuple(triplet) not in triplet_set:
                        triplets.append([nums[i],nums[j],nums[k]])
                        triplet_set.add(tuple(triplet))
                    j+=1
                elif curr > target:
                    k-=1
                else:
                    j+=1
            return

        for i in range(len(nums)):
            two_sum(i)
        
        return triplets