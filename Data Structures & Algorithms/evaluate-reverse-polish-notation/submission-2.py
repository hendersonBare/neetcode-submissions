class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        
        for i in range(len(tokens)):
            if tokens[i] == "+":
                op2 = int(num_stack.pop())
                op1 = int(num_stack.pop())
                num_stack.append(op1 + op2)
            elif tokens[i] == "*":
                op2 = int(num_stack.pop())
                op1 = int(num_stack.pop())
                num_stack.append(op1 * op2)
            elif tokens[i] == "/":
                op2 = int(num_stack.pop())
                op1 = int(num_stack.pop())
                num_stack.append(op1 / op2)
            elif tokens[i] == "-":
                op2 = int(num_stack.pop())
                op1 = int(num_stack.pop())
                num_stack.append(op1 - op2)
            else:
                num_stack.append(int(tokens[i]))

        return int(num_stack.pop())