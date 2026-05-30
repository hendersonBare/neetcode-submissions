class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}
        count_list = [[] for i in range(len(nums)+1)]
        #populate the map
        for i in range(len(nums)):
            if nums[i] in mapping:
                mapping[nums[i]] += 1
            else:
                mapping[nums[i]] = 1
        for num,count in mapping.items():
            count_list[count].append(num)
        res_list = []
        for i in range(len(count_list)-1,-1,-1):
            for j in range(len(count_list[i])):
                res_list.append(count_list[i][j])
                if len(res_list) == k:
                    return res_list
        return res_list
