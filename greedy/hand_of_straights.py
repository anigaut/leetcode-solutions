from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand.sort()
        counts = Counter(hand)

        for card in hand:
            if counts[card] > 0:
                counts[card] -= 1
                for next in range(card + 1, card + groupSize):
                    if next not in counts or counts[next] == 0:
                        return False
                    counts[next] -= 1
        
        return True

sol = Solution()
test_cases = [
    ([1,2,3,6,2,3,4,7,8], 3),
    ([1,2,3,4,5], 4)
]

for case in test_cases:
    print(sol.isNStraightHand(case[0], case[1]))
            
        