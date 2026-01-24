class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)
        highest_power = 1

        for i in range(1, n + 1):
            if i == highest_power * 2:
                highest_power = i
            output[i] = 1 + output[i - highest_power]
