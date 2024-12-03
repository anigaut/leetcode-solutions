'''
Create a hashmap for both input strings. 
Find the minimum substring for which both maps have the same letters and the count of each letter in s should be greater than or equal to the count for each letter in t.
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_map, t_map = {}, {}
        left = 0
        res_indices = [-float('inf'), float('inf')]

        for char in t:
            t_map[char] = t_map.get(char, 0) + 1
        
        s_map_len, t_map_len = 0, len(t_map)
        
        for right in range(len(s)):
            current = s[right]
            s_map[current] = s_map.get(current, 0) + 1

            if current in t_map and t_map[current] == s_map[current]:
                s_map_len += 1
            
            while s_map_len == t_map_len:
                if right - left + 1 < res_indices[1] - res_indices[0] + 1:
                    res_indices = [left, right]
                
                left_char = s[left]
                s_map[left_char] -= 1

                if left_char in t_map and s_map[left_char] < t_map[left_char]:
                    s_map_len -= 1

                left += 1
                    
        return s[res_indices[0] : res_indices[1] + 1] if res_indices != [-float('inf'), float('inf')] else ""