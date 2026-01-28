from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1

        seen = set()

        for row in range(n + 1):
            for col in range(n + 1):
                if (row, col) not in seen:
                    matrix[row][col], matrix[col][n - row] = (
                        matrix[col][n - row],
                        matrix[row][col],
                    )
                    seen.add((col, n - row))
        print(matrix)


sol = Solution()
test_cases = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
]
for case in test_cases:
    print(sol.rotate(case))
