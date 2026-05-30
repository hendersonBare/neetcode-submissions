# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if len(pairs) > 0:
            step_list = [pairs.copy()]
        else:
            return []
        curr_list = pairs.copy()
        for i in range(1, len(pairs)):
            j = i-1
            k = i
            while(curr_list[j].key > curr_list[k].key and j > -1 and k > j):
                #swap the 2 indices
                temp = curr_list[j]
                curr_list[j] = curr_list[k]
                curr_list[k] = temp
                j -= 1
                k -= 1
            step_list.append(curr_list.copy())
        return step_list