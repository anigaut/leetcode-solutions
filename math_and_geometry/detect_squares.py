from collections import defaultdict
from typing import List


class DetectSquares:

    def __init__(self):
        self.points = []
        self.points_count = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.points_count[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0

        for x, y in self.points:
            if abs(px - x) == abs(py - y) and px != x and py != y:
                res += self.points_count[(px, y)] * self.points_count[(x, py)]
        
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)