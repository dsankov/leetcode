class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        groups = defaultdict(list)
        for i, num in enumerate(nums):
            groups[num].append(i)

        arr = [0] * len(nums)
        for group in groups.values():
            m = len(group)
            if m == 1:
                continue
            total_sum = sum(group)
            left_sum = 0
            for i, idx in enumerate(group):
                right_sum = total_sum - left_sum - idx
                intervals_sum = i * idx - left_sum + right_sum - (m - 1 - i) * idx
                arr[idx] = intervals_sum
                left_sum += idx
        return arr