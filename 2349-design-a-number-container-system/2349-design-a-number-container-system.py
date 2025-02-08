class NumberContainers:

    def __init__(self):
        self.num_to_indices = defaultdict(list)
        self.index_to_num = {}
        

    def change(self, index: int, number: int) -> None:
        self.index_to_num[index] = number
        heapq.heappush(self.num_to_indices[number], index)

    
    def find(self, number: int) -> int:
        if not self.num_to_indices[number]:
            return -1
        
        while self.num_to_indices[number]:
            idx = self.num_to_indices[number][0]
            if self.index_to_num[idx] == number:
                return idx
            heapq.heappop(self.num_to_indices[number])
        
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)