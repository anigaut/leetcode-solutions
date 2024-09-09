def basic_calculator(s):
    stack = []
    for item in s:
        if item == " " or item == ")" or item == "(":
            continue
        elif item == "+" or item == "-":
            cur_op = item
        else:
            stack.append(int(item))
            if stack and len(stack) == 2:
                if cur_op == "+":
                    stack.append(stack.pop() + stack.pop())
                else:
                    diff = stack[-2] - stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(diff)

    return stack[-1]


s = "1 + 1"
s2 = " 2-1 + 2 "
s3 = "(1+(4+5+2)-3)+(6+8)"
print(basic_calculator(s3))
