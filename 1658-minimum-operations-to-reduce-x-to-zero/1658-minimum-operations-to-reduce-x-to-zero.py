class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        prefix_sums = [0]
        for num in nums:
            prefix_sums.append(num + prefix_sums[-1])
        desired_sum = prefix_sums[-1] - x
        if desired_sum < 0:
            return -1
        if desired_sum == 0:
            return n
            
        left = right = 0
        max_len = -1
        while right <= n:
            sub_sum = prefix_sums[right] - prefix_sums[left]
            if sub_sum == desired_sum:
                max_len = max(max_len, right - left)
                right += 1
            elif sub_sum < desired_sum:
                right += 1
            else:
                left += 1
        return n - max_len if max_len > 0 else -1


        