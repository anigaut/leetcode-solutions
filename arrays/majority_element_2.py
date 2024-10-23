# Based on Boyer-Moore's voting algorithm
# Remember that only 2 elements could each appear more then n/3 times
# Need to do 2 passes on the input array since finding the two most frequent elements doesn't capture their respective counts 

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, cand2 = None, None
        count1, count2 = 0, 0
        maj_elements = []

        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        count1, count2 = 0, 0
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
        
        if count1 > len(nums) // 3:
            maj_elements.append(cand1)
        if count2 > len(nums) // 3:
            maj_elements.append(cand2)
        
        return maj_elements
