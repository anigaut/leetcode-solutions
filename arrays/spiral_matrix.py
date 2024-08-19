class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0,len(matrix[0])
        top, bottom = 0, len(matrix)
        final = []

        while left < right and top < bottom:
            # Iterate through the top row
            for i in range(left, right):
                final.append(matrix[top][i])
            top += 1

            # Iterate through the right-most column
            for i in range(top, bottom):
                final.append(matrix[i][right - 1])
            right -= 1

            # Crucial condition that checks if all the elements have already been included in the output
            if not (left < right and top < bottom):
                break
            
            # Iterate through the bottom row
            for i in range(right - 1, left - 1, -1):
                final.append(matrix[bottom - 1][i])
            bottom -= 1

            # Iterate through the left-most column
            for i in range(bottom - 1, top - 1, -1):
                final.append(matrix[i][left])
            left += 1
        
        return final
        





