'''
- Initialize a hash map and iterate through the input array.
  
- In the map, maintain the difference between the current element and the target as the key, and the value as the index of the current element.
  
- Time Complexity: $O(n)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}

        for index in range(len(nums)):
            current = nums[index]
            if current in diffs:
                return [index, diffs[current]]
            else:
                diffs[target - current] = index


