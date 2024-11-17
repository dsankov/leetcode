class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return 1 if nums[0] >= k else -1

        prefix_sums = [0] * (n+1)
        for i in range(1, n+1):
            prefix_sums[i] = prefix_sums[i-1] + nums[i-1]

        decreasing_prefix_sum_indices_queue = deque()
        min_subarray_length = inf

        for i in range(n + 1):
            while (
                decreasing_prefix_sum_indices_queue
                and prefix_sums[i] - prefix_sums[decreasing_prefix_sum_indices_queue[0]] >= k
            ):
                    min_subarray_length = min(min_subarray_length, i - decreasing_prefix_sum_indices_queue[0])
                    decreasing_prefix_sum_indices_queue.popleft()

            while (
                decreasing_prefix_sum_indices_queue
                and prefix_sums[decreasing_prefix_sum_indices_queue[-1]] >= prefix_sums[i]
            ):
                    decreasing_prefix_sum_indices_queue.pop()
                    
            decreasing_prefix_sum_indices_queue.append(i)

        return min_subarray_length if min_subarray_length < inf else -1