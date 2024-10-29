# Shift the left pointer when the profit is negative - use while loop

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        left = 0

        for right in range(len(prices)):
            while prices[right] - prices[left] < 0:
                left += 1
            
            max_prof = max(max_prof, prices[right] - prices[left])

        return max_prof