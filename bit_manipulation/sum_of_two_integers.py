class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while b & mask > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        return (a & mask) if b > 0 else a


sol = Solution()
test_cases = [(1, 2), (2, 3)]
for case in test_cases:
    print(sol.getSum(case[0], case[1]))
