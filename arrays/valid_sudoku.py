'''
- Hash maps that contain the elements of each row, column and box that have already been looked at.
  
- Time complexity is $O(1)$ since the board is of fixed size.
'''


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        
        def which_box(row, col):
            if (0 <= row <= 2):
                if (0 <= col <= 2):
                    return 1
                elif (3 <= col <= 5):
                    return 2
                else:
                    return 3
            elif (3 <= row <= 5):
                if (0 <= col <= 2):
                    return 4
                elif (3 <= col <= 5):
                    return 5
                else:
                    return 6
            else:
                if (0 <= col <= 2):
                    return 7
                elif (3 <= col <= 5):
                    return 8
                else:
                    return 9
        
        row_nums = defaultdict(lambda: set())
        col_nums = defaultdict(lambda: set())
        box_nums = defaultdict(lambda: set())

        for row in range(9):
            for col in range(9):
                current = board[row][col]

                if (current in row_nums[row]):
                    return False
                elif (current != "."):
                    row_nums[row].add(current)
                
                if (current in col_nums[col]):
                    return False
                elif (current != "."):
                    col_nums[col].add(current)
                
                box = which_box(row, col)
                if current in box_nums[box]:
                    return False
                elif current != ".":
                    box_nums[box].add(current)

        return True       
