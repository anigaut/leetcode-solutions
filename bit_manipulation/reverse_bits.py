class Solution:
    def reverseBits(self, n: int) -> int:
        bin_form = bin(n)[2:].zfill(32)
        res = 0
        for i in range(len(bin_form)):
            res += int(bin_form[i]) * 2**i

        return res


sol = Solution()
test_cases = [43261596, 2147483644]
for case in test_cases:
    print(sol.reverseBits(case))
