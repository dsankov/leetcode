class SmallestInfiniteSet:

    def __init__(self):
        self.heap = list(range(1, 1001))
        self.set = set(self.heap)
        heapq.heapify(self.heap)

    def popSmallest(self) -> int:
        smallest_number = heapq.heappop(self.heap)
        self.set.remove(smallest_number)
        return smallest_number

    def addBack(self, num: int) -> None:
        if num not in self.set:
            self.set.add(num)
            heapq.heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)