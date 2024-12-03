'''
All 26 alphabets can occur in s. 

For each unique character in the input string, go through the string and compute the longest substring where that character won't be subsituted.
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        unique = set()
        for char in s:
            if char not in unique:
                unique.add(char)
        
        longest = 0
        for current in unique:
            left, replaced = 0, 0
            for i in range(len(s)):
                if s[i] != current:
                    replaced += 1

                while replaced > k:
                    if s[left] != current:
                        replaced -= 1
                    left += 1
                
                longest = max(longest, right - left + 1)
        
        return longest
