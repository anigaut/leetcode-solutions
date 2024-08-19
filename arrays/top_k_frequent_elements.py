'''
- Create a reversed hash-map, with frequency being the key and a list of each element that appears that many times as the value.
  
- The greatest possible key in the above hashmap is the size of the input array.
  
- Time complexity: $O(n)
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        reverse_counts = {}
        for i in range(len(nums), 0, -1):
            reverse_counts[i] = []
        
        for key in counts.keys():
            reverse_counts[counts[key]].append(key)
        
        top_k = []
        for count in reverse_counts:
            if reverse_counts[count]:
                top_k += reverse_counts[count]
     
        return top_k[:k]
