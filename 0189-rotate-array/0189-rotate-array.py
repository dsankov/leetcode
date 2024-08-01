class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        cycle_groups = math.gcd(n, k)
        for start_position in range(cycle_groups):
            write_position = (start_position + k) % n
            transit_num = nums[start_position]
            while write_position != start_position:
                nums[write_position], transit_num = transit_num, nums[write_position]
                write_position = (write_position + k) % n
            nums[start_position] = transit_num   # start_position == write_position