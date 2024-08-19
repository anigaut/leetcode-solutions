'''
- Create a hash map containing the sorted (alphabetical order) version of each string in the input array.
  
- While iterating through the array, if the sorted version of the current string already exists, append the string to that group.
  
- Time Complexity: $O(m*nlogn)$, where $m$ is the length of the input array and $n$ is the length of each individual string.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            word_sorted = ''.join(sorted(word))
            if word_sorted in groups:
                groups[word_sorted].append(word)
            else:
                groups[word_sorted] = [word]
        
        final = []
        for anagram in groups:
            final.append(groups[anagram])
        
        return final
