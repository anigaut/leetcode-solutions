class Solution:
    def checkValidString(self, s: str) -> bool:
        opening, stars = [], []

        for i in range(len(s)):
            char = s[i]

            if char == "(":
                opening.append(i)
            elif char == ")":
                if opening:
                    opening.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
            else:
                stars.append(i)
        
        while opening:
            if stars and stars[-1] >= opening[-1]:
                opening.pop()
                stars.pop()
            else:
                return False
        
        return True


sol = Solution()
test_cases = [
    "()", "(*)", "(*))", 
    "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()",
    "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"]

for case in test_cases:
    print(sol.checkValidString(case))