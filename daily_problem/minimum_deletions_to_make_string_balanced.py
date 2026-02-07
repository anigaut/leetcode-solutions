class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_before = 0
        a_after = s.count("a")
        min_deletions = a_after

        for letter in s:
            if letter == "b":
                b_before += 1
            else:
                a_after -= 1
            min_deletions = min(min_deletions, b_before + a_after)
        
        return min_deletions