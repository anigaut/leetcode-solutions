# Straightforward problem - only catch is when the given timestamp in the get method isn't there in the hashmap

class TimeMap:

    def __init__(self):
        self.vals = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.vals:
            self.vals[key] = []
        self.vals[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        cur_vals = [] if not key in self.vals else self.vals[key]
        left = 0
        right = len(cur_vals) - 1

        while left <= right:
            mid = (left + right) // 2
            if cur_vals[mid][1] <= timestamp:
                res = cur_vals[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        
        return res