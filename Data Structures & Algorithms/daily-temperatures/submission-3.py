class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indx_stack = []
        temp_stack = []
        results = [0 for i in range(len(temperatures))]

        for i in range(len(temperatures)):
            while len(temp_stack) > 0 and temp_stack[-1] < temperatures[i]:
                temp_stack.pop()
                indx = indx_stack.pop()
                results[indx] = i-indx
            temp_stack.append(temperatures[i])
            indx_stack.append(i)
        return results