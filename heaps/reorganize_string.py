from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        letter_counts = Counter(s)
        max_heap = []

        for letter in letter_counts:
            heapq.heappush(max_heap, (-1 * letter_counts[letter], letter))
        
        recon_s = ""

        prev_count, prev_letter = 0, ""

        while max_heap:
            count, letter = heapq.heappop(max_heap)
            recon_s += letter

            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_letter))
            
            prev_count, prev_letter = count + 1, letter
        
        if len(recon_s) != len(s):
            return ""
        
        return recon_s
            

        
