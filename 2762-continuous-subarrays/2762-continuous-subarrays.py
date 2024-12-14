class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        max_queue = deque()
        min_queue = deque()
        left = 0
        result = 0

        for right, num in enumerate(nums):
            while max_queue and nums[max_queue[-1]] < num:
                max_queue.pop()
            max_queue.append(right)

            while min_queue and nums[min_queue[-1]] > num:
                min_queue.pop()
            min_queue.append(right)

            while max_queue and min_queue and nums[max_queue[0]] - nums[min_queue[0]] > 2:
                if max_queue[0] < min_queue[0]:
                    left = max_queue[0] + 1
                    max_queue.popleft()
                else:
                    left = min_queue[0] + 1
                    min_queue.popleft()
            result += right - left + 1

        return result

        