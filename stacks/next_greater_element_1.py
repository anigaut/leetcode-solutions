# Iterate through the second array and each time you come across an element which is the next-greatest of an element in the first array, add it to the output array
# Maintain a stack to track all the elements that have been seen so far and pop elements as and when their next-greatest is found

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        stack = []
        nums1_idx = {}
        for ind, val in enumerate(nums1):
            nums1_idx[val] = ind

        for i in range(len(nums2)):
            current = nums2[i]
            while stack and current > stack[-1]:
                res[nums1_idx[stack.pop()]] = current
            
            if current in nums1_idx:
                stack.append(current)
        
        return res
