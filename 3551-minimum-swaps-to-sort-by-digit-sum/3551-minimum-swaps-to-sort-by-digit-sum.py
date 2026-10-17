class Solution:
    def minSwaps(self, nums: List[int]) -> int:
      
        n = len(nums)
        sorted_nums = sorted(nums, key=lambda x: (sum(map(int, str(x))), x))
        val_to_sorted_pos = {val: i for i, val in enumerate(sorted_nums)}
        visited = [False] * n
        cycles = 0
        for i in range(n):
            if not visited[i]:
                cycles += 1
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = val_to_sorted_pos[nums[j]]
        return n - cycles