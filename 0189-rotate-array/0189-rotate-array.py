class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        groups = math.gcd(n, k)
        for start in range(groups):
            write = (start + k) % n
            prev_num = nums[start]
            while write != start:
                save_num = nums[write]
                nums[write] = prev_num
                prev_num = save_num
                write = (write + k) % n
            nums[write] = prev_num