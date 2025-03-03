class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than_pivot = []
        greater_than_pivot = []
        pivot_count = 0
        for num in nums:
            if num < pivot:
                less_than_pivot.append(num)
            elif num > pivot:
                greater_than_pivot.append(num)
            else:
                pivot_count += 1

        return less_than_pivot + [pivot] * pivot_count + greater_than_pivot
        