from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_capacity = max(weights)
        max_capacity = sum(weights)

        while min_capacity < max_capacity:
            mid_capacity = (min_capacity + max_capacity) // 2
            cur_days = 1
            cur_capacity = 0

            for weight in weights:
                if cur_capacity + weight > mid_capacity:
                    cur_days += 1
                    cur_capacity = 0
                cur_capacity += weight

            if cur_days > days:
                min_capacity = mid_capacity + 1
            else:
                max_capacity = mid_capacity
        
        return min_capacity