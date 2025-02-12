class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        digit_sums = defaultdict(list)
        for num in nums:
            digit_sum = sum(int(digit) for digit in str(num))
            digit_sums[digit_sum].append(num)

        max_sum = -1
        for digit_sum, sum_nums in digit_sums.items():
            if len(sum_nums) >= 2:
                heapq.heapify(sum_nums)
                max_sum = max(max_sum, sum(heapq.nlargest(2, sum_nums)))
        return max_sum
        