class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for i in range(0, len(nums)+1)]
        for x in nums:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1
        for key, value in counts.items():
            freq[value].append(key)
        retArr = []
        for i in range(len(freq) - 1, 0, -1):
            for x in freq[i]:
                retArr.append(x)
                if len(retArr) == k:
                    return retArr
