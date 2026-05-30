class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indstack = []
        valstack = []
        ret = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if len(indstack) == 0 or len(valstack) == 0:
                indstack.append(i)
                valstack.append(temperatures[i])
            else:
                while len(valstack) > 0 and temperatures[i] > valstack[-1]:
                    valstack.pop()
                    start = indstack.pop()
                    distance = i - start
                    ret[start] = distance
                valstack.append(temperatures[i])
                indstack.append(i)
        return ret
