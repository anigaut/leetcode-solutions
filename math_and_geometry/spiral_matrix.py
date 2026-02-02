from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []
        top_row, bottom_row = 0, m - 1
        first_col, last_col = 0, n - 1

        while True:
            for col in range(first_col, last_col + 1):
                res.append(matrix[top_row][col])
            top_row += 1

            if len(res) == m * n:
                break

            for row in range(top_row, bottom_row + 1):
                res.append(matrix[row][last_col])
            last_col -= 1

            if len(res) == m * n:
                break

            for col in range(last_col, first_col - 1, -1):
                res.append(matrix[bottom_row][col])
            bottom_row -= 1

            if len(res) == m * n:
                break

            for row in range(bottom_row, top_row - 1, -1):
                res.append(matrix[row][first_col])
            first_col += 1

            if len(res) == m * n:
                break
        
        return res

sol = Solution()
test_cases = [
    [[1,2,3],[4,5,6],[7,8,9]],
    [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
]

for case in test_cases:
    print(sol.spiralOrder(case))
            

