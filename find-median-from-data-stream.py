from heapq import heappop, heappush


class MedianFinder:

    def __init__(self):
        self.min_heap = [] # right side
        self.max_heap = [] # left side
        self.count = 0
        

    def addNum(self, num: int) -> None:
        self.count += 1
        heappush(self.max_heap, -num)
        if self.count % 2 == 0:
            top = heappop(self.max_heap)
            heappush(self.min_heap, -top)
        else:
            if self.min_heap and -self.max_heap[0] > self.min_heap[0]:
                lm = -heappop(self.max_heap)
                rm = heappop(self.min_heap)
                heappush(self.min_heap, lm)
                heappush(self.max_heap, -rm)

    def findMedian(self) -> float:
        if self.count %2 == 1:
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())