import heapq

class MedianFinder:

    def __init__(self):
        self.first_half = []
        self.second_half = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.first_half, -num)

        if self.first_half and self.second_half and -self.first_half[0] > self.second_half[0]:
            val = -heapq.heappop(self.first_half)
            heapq.heappush(self.second_half, val)
        
        if len(self.first_half) > len(self.second_half) + 1:
            val = -heapq.heappop(self.first_half)
            heapq.heappush(self.second_half, val)
        
        if len(self.second_half) > len(self.first_half) + 1:
            val = heapq.heappop(self.second_half)
            heapq.heappush(self.first_half, -val)

    def findMedian(self) -> float:
        if len(self.first_half) == len(self.second_half):
            return (-self.first_half[0] + self.second_half[0]) / 2
        elif len(self.first_half) > len(self.second_half):
            return -self.first_half[0]
        else:
            return self.second_half[0]