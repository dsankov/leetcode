class Solution:
    def trap(self, heights: List[int]) -> int:

        left, right = 0, len(heights) - 1
        left_max, right_max = heights[left], heights[right]
        total_water_amount = 0
        while left <= right:            
            if left_max < right_max:
                left_max = max(left_max, heights[left])
                total_water_amount += left_max - heights[left]
                left += 1
            else:
                right_max = max(right_max, heights[right])
                total_water_amount += right_max - heights[right]
                right -= 1

        return total_water_amount