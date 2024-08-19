class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        - Can't use hash tables since it has to be done in-place.
        - For every 0 element, mark the first element of it's row and column to signify that the entire row and column must be made 0
        - This can be tricky since matrix[0][0] is the first element of the first row and column.
        """
        rows, cols = len(matrix), len(matrix[0])

        # verifies if the first row has zero
        first_row_zero = True if 0 in matrix[0] else False 
        
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = "c"
                    if row > 0:
                        matrix[row][0] = "r"
        
        for col in range(cols):
            if matrix[0][col] == "c":
                for row in range(rows):
                    if matrix[row][col] != "r":
                        matrix[row][col] = 0
        
        for row in range(1, rows):
            if matrix[row][0] == "r":
                for col in range(cols):
                    matrix[row][col] = 0
        
        if first_row_zero:
            matrix[0] = [0 for i in range(len(matrix[0]))]