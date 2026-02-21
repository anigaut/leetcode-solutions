from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack, res = [], []

        for ast in asteroids:
            if ast > 0:
                stack.append(ast)
            else:
                same_size = False
                while stack:
                    if abs(ast) > stack[-1]:
                        stack.pop()
                    elif stack[-1] > abs(ast):
                        break
                    else:
                        stack.pop()
                        same_size = True
                        break
                
                if not stack and not same_size:
                    res.append(ast)

        for ast in stack:
            res.append(ast)
        
        return res

sol = Solution()
test_cases = [[5,10,-5], [8,-8], [10,2,-5], [3,5,-6,2,-1, 4]]
for case in test_cases:
    print(sol.asteroidCollision(case))