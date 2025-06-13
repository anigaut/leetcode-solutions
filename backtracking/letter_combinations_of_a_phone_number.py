'''
- Don't overcomplicate the problem. 
- Draw a tree to visualize the combinations.
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def backtrack(i, cur):
            if len(cur) == len(digits):
                res.append(str(cur))
                return
            
            for char in digit_map[digits[i]]:
                backtrack(i + 1, cur + char)

        if digits:
            backtrack(i=0, cur="")
        return res