# Using a separate array for 1, max(piles) to perform the binary search will exceed the memory limit
# Perform the binary search implicitly

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        left, right = 1, max(piles)
        min_speed = max(piles)
        while left <= right:
            cur_speed = (left + right) // 2
            cur_time = 0

            for pile in piles:
                cur_time += math.ceil(pile / cur_speed)
            
            if cur_time <= h:
                min_speed = min(min_speed, cur_speed)
                right = cur_speed - 1
            else:
                left = cur_speed + 1
        return min_speed


    

