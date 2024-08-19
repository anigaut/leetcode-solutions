# - Create a Hash Map (Dictionary in Python) containing all elements of the input array.
#
# - Iterate through the list. If you come across an element that is already present in the dictionary, return True.
#
# - Time complexity: $O(n)
#


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_count = {}
        for num in nums:
            if num in num_count:
                return True
            else:
                num_count[num] = 1
        return False
