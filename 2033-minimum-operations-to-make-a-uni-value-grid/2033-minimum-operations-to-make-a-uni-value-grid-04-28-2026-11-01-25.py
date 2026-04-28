class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = list(itertools.chain.from_iterable(grid))
        n = len(nums)
        nums.sort()
        rem = nums[0] % x
        if any(num % x != rem for num in nums):
            return -1

        nums = [num // x for num in nums]
        min_num, max_num = min(nums), max(nums)
        if min_num == max_num:
            return 0
        deviations = [(num - min_num) / (max_num - min_num) for num in nums ]
        center = sum(deviations) / n
        center_id = round(center * n)
        center_num = nums[center_id]
        distance = sum(abs(center_num - num) for num in nums)
        return distance
