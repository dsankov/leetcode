class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def num_bits(x: int) -> int:
            return sum(int(bit) for bit in f"{x:b}")
        prev_segment_max = -math.inf
        curr_segment_mask = num_bits(nums[0])
        curr_segment_max = -math.inf
        for num in nums:
            if num_bits(num) == curr_segment_mask:
                curr_segment_max = max(curr_segment_max, num)
            else:
                prev_segment_max = curr_segment_max
                curr_segment_max = num
                curr_segment_mask = num_bits(num)
            if num < prev_segment_max:
                return False

        return True
            
        