'''
- Iterate through s2, maintaining a window of size len(s1)
- If any such window's permutation matches s1, return true
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        s2_map = {}

        for letter in s1:
            s1_map[letter] = s1_map.get(letter, 0) + 1
        
        left = 0
        
        for right in range(len(s2)):
            s2_map[s2[right]] = s2_map.get(s2[right], 0) + 1

            if s2_map == s1_map:
                return True
            
            if right - left + 1 == len(s1):
                left_char = s2[left]
                s2_map[left_char] -= 1
                if s2_map[left_char] == 0:
                    s2_map.pop(left_char)
                left += 1

        return False