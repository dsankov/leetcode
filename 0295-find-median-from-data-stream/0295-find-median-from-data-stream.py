class MedianFinder:

    def __init__(self):
        self.upper_half = []
        self.lower_half = []
        

    def addNum(self, num: int) -> None:
        if len(self.lower_half) == len(self.upper_half):
            heappush(self.upper_half, num)
            return
        if num >= self.upper_half[0]:
            low_bound = heappushpop(self.upper_half, num)
            heappush(self.lower_half, -low_bound)
        else:
            high_bound = - heappushpop(self.lower_half, -num)
            heappush(self.upper_half, high_bound)
        

    def findMedian(self) -> float:
        if len(self.lower_half) != len(self.upper_half):
            return self.upper_half[0]
        return (self.upper_half[0] - self.lower_half[0]) / 2.0

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()