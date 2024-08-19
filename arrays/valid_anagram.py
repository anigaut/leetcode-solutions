'''
- Create a hash map for both input words, containing each letter of the word and the number of times it appears.
  
- If the respective maps are identical, the words are anagrams.
  
- Time complexity: $O(n)
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def letter_counts(word):
            counts = {}
            for letter in word:
                if letter in counts:
                    counts[letter] += 1
                else:
                    counts[letter] = 1
            return counts
        
        s_letter_counts = letter_counts(s)
        t_letter_counts = letter_counts(t)

        if s_letter_counts == t_letter_counts:
            return True
        else:
            return False

