# Definitely not the most efficient way to write the code - plenty of repetiton

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                res = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
            elif token == "*":
                res = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
            elif token == "/":
                res = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(res)
            elif token == "-":
                res = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
            else:
                stack.append(int(token))
        
        return stack[-1]
