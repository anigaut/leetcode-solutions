'''
Find out each sequence in the list and the number it starts with. From each of them, find out the longest sequence.
'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums:
            if num -1 not in nums_set:
                current = num
                sequence = 1
                while current + 1 in nums_set:
                    sequence += 1
                    current += 1
                longest = max(longest, sequence)
        
        return longest
        