class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n == 1:
            return False

        index = -1
        current_prefix_sum = 0
        prefix_sums = {current_prefix_sum: index}

        for index in range(n):
            number = nums[index] % k
            current_prefix_sum = (current_prefix_sum + number) % k
            if current_prefix_sum in prefix_sums:
                if index - prefix_sums[current_prefix_sum] > 1:
                    return True
            else:
                prefix_sums[current_prefix_sum] = index

        return False

     