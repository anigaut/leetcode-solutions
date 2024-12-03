'''
Keep a tab of the number of zeroes in the current window

When the number of zeroes exceeds k, bring the left pointer forward until the number of zeroes goes below k again
'''

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        longest_seq = 0
        zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
                while zero_count > k:
                    if nums[left] == 0:
                        zero_count -= 1
                    left += 1
            
            longest_seq = max(longest_seq, right - left + 1)
        
        return longest_seq