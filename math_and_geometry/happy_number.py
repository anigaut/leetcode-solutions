class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares_of_digits(num):
            res = 0
            while num > 0:
                res += (num % 10) ** 2
                num = num // 10
            
            return res
        
        seen = set()

        while n not in seen:
            seen.add(n)
            n = sum_of_squares_of_digits(n)
            if n == 1:
                return True
        
        return False