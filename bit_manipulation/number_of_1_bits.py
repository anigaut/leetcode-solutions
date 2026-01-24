class Solution:
    def hammingWeight(self, n: int) -> int:
        quo, rem = n, None
        res = 0

        while quo != 0:
            rem = quo % 2
            quo = quo // 2

            if rem == 1:
                res += 1

        return res


sol = Solution()
test_cases = [11, 128, 2147483645]
for case in test_cases:
    print(sol.hammingWeight(case))
