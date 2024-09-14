# Look at each 'tower' on its own and see how far it can stretch both ways
# Maintain a monotonically increasing stack
# When you come across a number less than the top of the stack, iterate through the stack to find how far to the left the new element can go

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for ind, height in enumerate(heights):
            start_ind = ind
            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                max_area = max(max_area, h * (ind - i))
                start_ind = i
            stack.append((start_ind, height))
        
        for ind, height in stack:
            max_area = max(max_area, height * (len(heights) - ind))
        return max_area 
