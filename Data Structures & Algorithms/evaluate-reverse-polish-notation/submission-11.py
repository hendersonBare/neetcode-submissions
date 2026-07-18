class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==1:
            return int(tokens[0])
        stack = tokens[::-1]
        ops = {"+", "-", "*", "/"}

        vals = []
        while len(stack)>0:
            while stack[-1] not in ops:
                vals.append(stack.pop())
            
            print(vals)

            op = stack.pop()
            print("op: ", op)
            b = int(vals.pop())
            print("b: ", b)
            a = int(vals.pop())
            print("a: ", a)

            x=0

            match op:
                case "+":
                    x = a + b
                case "-":
                    x = a - b
                case "*":
                    x = a * b
                case "/":
                    x = int(a/b)

            print(x)
            
            vals.append(str(x))
            print(len(stack))

        return int(vals.pop())

