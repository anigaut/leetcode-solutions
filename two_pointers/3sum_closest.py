'''
Quite similar to 3sum, except that the three sum combination that is closest to the target needs to be tracked
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if abs(three_sum - target) < abs(closest_sum - target):
                    closest_sum = three_sum
                
                if three_sum == target:
                    return three_sum
                elif three_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum
    
