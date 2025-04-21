class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        max_add = 0
        min_add = 0
        running_add = 0

        for diff in differences:
            running_add += diff
            max_add = max(max_add, running_add)
            min_add = min(min_add, running_add)

        hidden_start  = lower - min_add
        hidden_end = upper - max_add
        return max(0, hidden_end - hidden_start + 1)