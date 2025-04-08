class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        num_present = [False] * 101
        for idx in range(n-1, -2, -1):
            if idx == -1:
                return 0
            if num_present[nums[idx]]:
                break
            num_present[nums[idx]] = True
        return (idx + 1) // 3 + (0 if (idx + 1) % 3 == 0 else 1)

        