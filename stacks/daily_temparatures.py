# Quite similar to Next Greater Element 1, but duplicate numbers are allowed in the input array, which means a hashmap cannot be used to maintain the indices of the numbers

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_idx = {}
        stack = []
        ind_stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            current = temperatures[i]
            while stack and current > stack[-1]:
                res[ind_stack[-1]] = i - ind_stack[-1]
                ind_stack.pop()
                stack.pop()
            stack.append(current)
            ind_stack.append(i)
        return res
