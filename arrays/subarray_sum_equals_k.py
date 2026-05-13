from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarray_sums = {0: 1}
        total = 0
        res = 0

        for num in nums:
            total += num

            if (total - k) in subarray_sums:
                res += subarray_sums[total - k]

            if total in subarray_sums:
                subarray_sums[total] += 1
            else:
                subarray_sums[total] = 1

        return res
