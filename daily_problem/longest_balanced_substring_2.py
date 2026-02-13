from collections import defaultdict


class Solution:
    def longestBalanced(self, s: str) -> int:
        def one_unique():
            res, start = 0, 0
            cur = s[0]
            for i in range(len(s)):
                letter = s[i]
                if letter != cur:
                    cur = letter
                    start = i
                res = max(res, i - start + 1)
            return res
        
        def two_unique(l1, l2):
            res = l1_count = l2_count = 0
            match = {0: -1}
            for i in range(len(s)):
                letter = s[i]
                if letter != l1 and letter != l2:
                    match.clear()
                    match = {0: i}
                    l1_count, l2_count = 0, 0
                else:
                    if letter == l1:
                        l1_count += 1
                    else:
                        l2_count += 1
                    
                    key = (l1_count - l2_count)
                    if key in match:
                        res = max(res, i - match[key])
                    else:
                        match[key] = i
            
            return res
        
        def all_three():
            res = a_count = b_count = c_count = 0
            match = {(0, 0): -1}
            for i in range(len(s)):
                letter = s[i]
                if letter == "a":
                    a_count += 1
                elif letter == "b":
                    b_count += 1
                else:
                    c_count += 1
            
                key = (a_count - c_count, b_count - c_count)

                if key in match:
                    res = max(res, i - match[key])
                else:
                    match[key] = i
            
            return res

        return(
            max(
                one_unique(),
                two_unique("a", "b"),
                two_unique("b", "c"),
                two_unique("a", "c"),
                all_three()
            )
        )

sol = Solution()
test_cases = ["abbac", "aabcc", "aba"]
for case in test_cases:
    print(sol.longestBalanced(case))              
                