class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.sum_matrix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            row_sum_until = 0
            for c in range(cols):
                row_sum_until += matrix[r][c]
                sum_above = self.sum_matrix[r][c + 1]
                self.sum_matrix[r + 1][c + 1] = row_sum_until + sum_above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottom_right = self.sum_matrix[row2 + 1][col2 + 1]
        above = self.sum_matrix[row1][col2 + 1]
        left = self.sum_matrix[row2 + 1][col1]
        top_left = self.sum_matrix[row1][col1]

        return bottom_right - above - left + top_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
