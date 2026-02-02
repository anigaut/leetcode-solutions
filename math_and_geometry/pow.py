class Solution:
    def myPow(self, x: float, n: int) -> float:
        is_neg = True if n < 0 else False
        if is_neg:
            n *= -1
        
        def breakdown(num, pow):
            if pow == 0:
                return 1
            if pow == 1:
                return num
            
            if pow % 2 == 0:
                temp = breakdown(num, pow // 2)
                return temp * temp
            else:
                temp = breakdown(num, (pow - 1) // 2)
                return temp * temp * num
        
        p = breakdown(x, n)

        return 1 / p if is_neg else p