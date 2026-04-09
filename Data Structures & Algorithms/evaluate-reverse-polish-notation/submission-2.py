class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # we push the res after each operation, back to the stack
        stack = []
        operators = ["+", "-", "*", "/"]
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                first = stack.pop()
                second = stack.pop()
                if i == "+":
                    res = first + second
                    stack.append(res)
                if i == "-":
                    res = second - first
                    stack.append(res)
                if i == "*":
                    res = first * second
                    stack.append(res)
                if i == "/":
                    # cast to an int auto truncate towards 0
                    res = int(second / first)
                    stack.append(res)
        return stack.pop()
                
