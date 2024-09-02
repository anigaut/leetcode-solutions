'''
- Parentheses must be closed in the correct order - for example, "([)]" is not valid
- The stack must therefore be non-empty when you come across a closing bracket.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in matches:
                if stack and stack[-1] == matches[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        if stack:
            return False
        return True 
