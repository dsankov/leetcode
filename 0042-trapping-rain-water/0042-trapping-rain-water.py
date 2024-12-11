class Solution:
    def trap(self, heights: List[int]) -> int:
        height_stack = []
        height_stack.append(heights[0])
        total_water_amount = 0


        for height in heights[1:]:
            curr_water_amount = 0
            occupied_cells = 0 
            curr_gap_width = 0
            prev_height = 0
            
            while height_stack and height_stack[-1] <= height:
                prev_height = height_stack.pop()
                occupied_cells += prev_height
                curr_gap_width += 1

            if height_stack:
                height_stack.extend([height] * curr_gap_width)
                curr_gap_height = height
            else:
                curr_gap_height = prev_height
            height_stack.append(height)

            curr_water_amount = curr_gap_width * curr_gap_height - occupied_cells
            total_water_amount += curr_water_amount

        return total_water_amount