class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_pq = [-num for num in nums]
        heapify(max_pq)
        next_max = 0
        result = 0
        while k > 0:
            k -= 1
            next_max = -heappop(max_pq)
            result += next_max
        
            heappush(max_pq, -(next_max // 3 + ( 0 if next_max % 3 == 0 else 1)))
        return result