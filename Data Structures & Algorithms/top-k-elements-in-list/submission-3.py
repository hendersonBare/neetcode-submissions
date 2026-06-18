class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = [[] for x in range(0,len(nums)+1)]

        value_map = defaultdict(int)
        for num in nums:
            value_map[num] += 1

        for x, count in value_map.items():
            counts[count].append(x)

        results = []

        for i in range(len(counts)-1,-1,-1):
            for val in counts[i]:
                results.append(val)
                if len(results) == k:
                    return results

        