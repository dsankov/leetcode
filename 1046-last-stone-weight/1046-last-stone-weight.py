class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_max_heap = [-stone for stone in stones]
        heapq.heapify(stones_max_heap)
        
        while len(stones_max_heap) > 1:
            first = -heapq.heappop(stones_max_heap)
            second = -heapq.heappop(stones_max_heap)
            if first > second:
                heapq.heappush(stones_max_heap, second-first)
        if len(stones_max_heap) == 1:
            return -stones_max_heap[0]
        return 0