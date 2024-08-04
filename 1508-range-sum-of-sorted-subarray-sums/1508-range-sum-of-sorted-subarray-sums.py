class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 10**9 + 7
        answer = 0
        sums_queue = []
        for i, num in enumerate(nums):
            heappush(sums_queue, (num, i))
        for i in range (1, right+1):
            min_sum, end_index = heappop(sums_queue)
            if i >= left:
                answer = (answer + min_sum) % mod
            if end_index < n - 1:
                sum = min_sum + nums[end_index+1]
                heappush(sums_queue, (sum, end_index+1))     
        return answer
        