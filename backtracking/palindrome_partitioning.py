'''
- Core logic is not very hard, but implementing that in code using backtracking and recursion is tricky.
- For each letter in the string, for each substring starting from that letter, check if it is a palindrome and whether substrings starting from the next letter can be partitioned into palindromes as well.
'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, cur = [], []

        def backtrack(i):
            if i >= len(s):
                res.append(cur[:])
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s[i : j + 1]):
                    cur.append(s[i : j + 1])
                    backtrack(j + 1)
                    cur.pop()
        
        backtrack(0)
        return res
        
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left + 1, right - 1
        return True