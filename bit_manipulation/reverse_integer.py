class Solution:
    def reverse(self, x: int) -> int:
        is_neg = True if x < 0 else False

        if is_neg:
            x *= -1

        res = 0

        while x > 0:
            last_digit = x % 10
            res = res * 10 + last_digit
            x = x // 10

        if res > 2**31:
            return 0

        return -1 * res if is_neg else res
