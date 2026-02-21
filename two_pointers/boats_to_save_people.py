from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        num_boats = 0
        cur_weight = num_people = 0

        while left <= right:
            num_boats += 1
            cur_weight += people[right]
            num_people += 1

            while cur_weight + people[left] <= limit and num_people < 2 and left < right:
                cur_weight += people[left]
                num_people += 1
                left += 1
            
            cur_weight = 0
            num_people = 0
            right -= 1
        
        return num_boats
        
sol = Solution()
test_cases = [
    ([1,2], 3), 
    ([3,2,2,1], 3), 
    ([3,5,3,4], 5), 
    ([5, 1, 4, 2], 6),
    ([2,49,10,7,11,41,47,2,22,6,13,12,33,18,10,26,2,6,50,10], 50)
]
for case in test_cases:
    print(sol.numRescueBoats(case[0], case[1]))