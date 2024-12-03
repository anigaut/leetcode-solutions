'''
Once all three elements have appeared at least once, count the number of substrings that begin and end from that index

Use the left pointer to calculate how many substrings appear before the index
'''

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        letter_counts = {}
        num_substrings = 0
        left = 0

        for right in range(len(s)):
            current = s[right]
            letter_counts[current] = letter_counts.get(current, 0) + 1

            while len(letter_counts) == 3 and left <= right:
                num_substrings += len(s) - right

                left_char = s[left]
                letter_counts[left_char] -= 1
                
                if letter_counts[left_char] == 0:
                    letter_counts.pop(left_char)
                
                left += 1
        
        return num_substrings