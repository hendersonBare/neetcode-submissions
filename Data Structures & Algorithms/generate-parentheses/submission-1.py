class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        stack = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                s = ""
                for c in stack:
                    s += c
                ret.append(s)
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN+1)
                stack.pop()
        
        backtrack(0,0)
        return ret