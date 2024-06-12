class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = Counter(nums)
        offset = 0
        for color in sorted(colors):
            for i in range(colors[color]):
                nums[offset + i] = color
            offset += colors[color]
            