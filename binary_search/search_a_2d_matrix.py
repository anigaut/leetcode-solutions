# Implement binary search on each row of the matrix
# Can also concatenate all rows into one mega list and apply binary search

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(array, targ):
            left = 0
            right = len(array) - 1
    
            while left <= right:
                mid = (left + right) // 2
                if targ == array[mid]:
                    return True
                elif targ > array[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
        
        for row in matrix:
            if binary_search(row, target):
                return True
        return False 
