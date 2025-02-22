import heapq

class MedianFinder:

    def __init__(self):
        #max heap, min heap
        self.small, self.large = [], []
        self.stream_length = 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        if self.small and self.large and (-self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))
        
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.large) < len(self.small):
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0])/2
        