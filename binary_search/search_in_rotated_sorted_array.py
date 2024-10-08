# Find the index of the pivot element. The sub-arrays on either side of it will be sorted
# Conduct binary search on both sides to check if the target element exists

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def find_min_index(arr):
            left, right = 0, len(arr) - 1
            while left < right:
                mid = (left + right) // 2
                if arr[mid] > arr[right]:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        def bin_search(arr, target, start, end):
            while start <= end:
                mid = (start + end) // 2
                if arr[mid] == target:
                    return mid
                if arr[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return - 1 

        min_index = find_min_index(nums)
        left_res = bin_search(nums, target, 0, min_index - 1)
        right_res = bin_search(nums, target, min_index, len(nums) - 1)
    
        if left_res != -1:
            return left_res
        elif right_res != -1:
            return right_res
        else:
            return -1 
