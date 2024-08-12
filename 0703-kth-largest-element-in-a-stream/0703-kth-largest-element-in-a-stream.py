class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k_largest = []
        self.k = k
        for num in nums:
            self.add(num)

        

    def add(self, val: int) -> int:
        if (len(self.k_largest) < self.k
            or val > self.k_largest[0]):
            heappush(self.k_largest, val)
            if len(self.k_largest) > self.k:
                heappop(self.k_largest)
        return self.k_largest[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)