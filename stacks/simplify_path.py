# Straightforward problem - need to deal with ".." and "." mainly

class Solution:
    def simplifyPath(self, path: str) -> str:
        path_array = path.split("/")
        simp_path = "/"
        stack = []
        for item in path_array:
            if item == "." or item == "":
                continue
            elif item == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(item)
        if stack:
            for item in stack[:-1]:
                simp_path += item + "/"
            simp_path += stack[-1]

        return simp_path
