# Use hashmap or hashset to keep track of seen letters
# The key lies in figuring out where the new substring should begin from when an item reappears
# Time complexity - O(n), space complexity - O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, i = 0, 0
        unique = set()

        for j in range(len(s)):
            while s[j] in unique:
                unique.remove(s[i])
                i += 1
            
            unique.add(s[j])
            longest = max(longest, j - i + 1)
        
        return longest