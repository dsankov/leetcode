class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        self.nums = sorted(nums)
        self.array_size = len(nums)

        left = 0
        right = self.nums[-1] - self.nums[0]

        while left < right:
            mid = left + (right - left) // 2
            count_pairs = self.count_pairs_with_distance_less_than(mid)

            if count_pairs < k:
                left = mid + 1
            else:
                right = mid
        return left

    def count_pairs_with_distance_less_than(self, distance):
        count_pairs = 0
        left = 0
        for right in range(self.array_size):
            while self.nums[right] - self.nums[left] > distance:
                left += 1
            count_pairs += right - left
        return count_pairs

        