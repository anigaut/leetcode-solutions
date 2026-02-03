class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        prods = []

        for i in range(len(num1) - 1, -1, -1):
            cur_prod, carry = 0, 0
            place = 1
            for j in range(len(num2) - 1, -1, -1):
                d1, d2 = int(num1[i]), int(num2[j])
                prod = (d1 * d2) + carry
                cur_prod += prod % 10 * place
                carry = prod // 10
                place *= 10
            
            cur_prod += carry * place
            prods.append(cur_prod)
        
        # print(prods)
        res = prods[0]
        mult = 10
        for i in range(1, len(prods)):
            res += prods[i] * mult
            mult *= 10

        return str(res)

sol = Solution()
test_cases = [("2", "3"), ("123", "456")]
for case in test_cases:
    print(sol.multiply(case[0], case[1]))