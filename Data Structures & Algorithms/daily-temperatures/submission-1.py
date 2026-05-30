class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret_arr = [0] * len(temperatures)
        temp_stack = []
        ind_stack = []
        for i in range(len(temperatures)):
            val = temperatures[i]
            if (len(temp_stack) == 0):
                temp_stack.append(val)
                ind_stack.append(i)
                continue
            while (len(temp_stack) > 0 and val > temp_stack[-1]):
                temp_stack.pop()
                ind = ind_stack.pop()
                ret_arr[ind] = i - ind
            temp_stack.append(val)
            ind_stack.append(i)
        return ret_arr


