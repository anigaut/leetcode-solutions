class Solution:
    def climbStairs(self, n: int) -> int:
        combos = {1: 1, 2: 2}
        
        def memoize(num):
            if num in combos:
                return combos[num]
            
            combos[num] = memoize(num - 1) + memoize(num - 2)
            return combos[num]
        
        return memoize(n)


test_cases = [1, 2, 3, 4, 5]
sol = Solution()
for case in test_cases:
    print(sol.climbStairs(case))