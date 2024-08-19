'''
- Make two passes through the array to calculate the prefix and postfix products for each element.
  
- Time complexity: $O(2n) = O(n).
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]
        prod = 1
        for i in range(len(nums) - 1):
            prod *= nums[i]
            pref.append(prod)
        
        post = [1]
        prod = 1
        for i in range(len(nums)-1, 0, -1):
            prod *= nums[i]
            post.append(prod)
        post.reverse()

        final = []
        for i in range(len(nums)):
            final.append(pref[i] * post[i])
        
        return final
