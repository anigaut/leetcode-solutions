# Based on Boyce-Moore's algorithm. Not intuitive, but very simple
# Hint: decrement the count when required

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        output, count = 0, 0

        for num in nums:
            if count == 0:
                output = num
                count = 1
            elif num == output:
                count += 1
            else:
                count -= 1
        
        return output