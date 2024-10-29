# This is the brute-force solution - not optimal - O(m * n) 
# Knuth-Morris-Pratt Algorithm is ideal - O(m+n), not sure how to do that yet

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1