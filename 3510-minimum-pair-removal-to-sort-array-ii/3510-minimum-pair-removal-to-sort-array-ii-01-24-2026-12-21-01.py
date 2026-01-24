class Solution:
    def init(self, nums):
        self.n = len(nums)
        self.removed = [False] * self.n
        self.prev_nums = [ptr - 1 for ptr in range(self.n)]
        self.next_nums = [ptr + 1 for ptr in range(self.n)]
        self.values = nums[:]

        self.inversions = sum(a > b for a, b in pairwise(self.values))
        print(self.inversions)
        self.sum_queue = [(a + b, idx) for idx, (a, b) in enumerate(pairwise(self.values))]
        heapify(self.sum_queue)
        
    def is_sorted(self):
        return self.inversions == 0

    def item_to_merge(self):
        while  self.sum_queue:
            cur_min_sum, idx = self.sum_queue[0]
            if (
                self.removed[idx] 
                or self.next_nums[idx] == self.n
                or self.values[idx] + self.values[self.next_nums[idx]] != cur_min_sum
                ):
                    heappop(self.sum_queue)
            else:
                    break
            
        if not self.sum_queue:
            return -1
        return heappop(self.sum_queue)[1]

    def merge(self, a):
        b = self.next_nums[a]
        if b == self.n:
            return
        updated_value = self.values[a] + self.values[b]

        before_a = self.prev_nums[a]
        after_b = self.next_nums[b]

        if self.values[a] > self.values[b]:
            self.inversions -= 1
        if before_a != -1 and self.values[before_a] > self.values[a]:
            self.inversions -= 1
        if after_b != self.n and self.values[b] > self.values[after_b]:
            self.inversions -= 1

        if before_a != -1 and self.values[before_a] > updated_value:
            self.inversions += 1
        if after_b != self.n and updated_value > self.values[after_b]:
            self.inversions += 1

        self.values[a] = updated_value
        self.removed[b] = True
        self.next_nums[a] = after_b
        if after_b != self.n:
            self.prev_nums[after_b] = a
            heappush(self.sum_queue, (self.values[a] + self.values[after_b], a))
        if before_a != -1:
            heappush(self.sum_queue, (self.values[before_a] + self.values[a], before_a))


    def minimumPairRemoval(self, nums: List[int]) -> int:

        self.init(nums)
        num_ops = 0
        while not self.is_sorted():
            position = self.item_to_merge()
            self.merge(position)
            num_ops += 1

        return num_ops 