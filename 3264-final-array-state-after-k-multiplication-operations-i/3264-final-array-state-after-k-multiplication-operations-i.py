class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        nums_queue = [(num, idx) for idx, num in enumerate(nums)]
        heapify(nums_queue)
        for _ in range(k):
            num, idx = heappop(nums_queue)
            heappush(nums_queue, (num * multiplier, idx))
        result = [0] * len(nums)
        for num, idx in nums_queue:
            result[idx] = num
        return result
        