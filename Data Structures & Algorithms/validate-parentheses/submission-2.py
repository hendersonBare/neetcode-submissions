class Solution:
    def isValid(self, s: str) -> bool:
        close = {}
        close[")"] = "("
        close["}"] = "{"
        close["]"] = "["
        stack = []

        for c in s:
            if c not in close:
                stack.append(c)
            if c in close:
                if len(stack) == 0:
                    return False
                if close[c] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
