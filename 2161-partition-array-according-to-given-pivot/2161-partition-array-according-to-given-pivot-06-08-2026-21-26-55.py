class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        exact = []
        more = []
        for num in nums:
            if num < pivot:
                less.append(num)
            elif pivot < num:
                more.append(num)
            else:
                exact.append(num)
        return less + exact + more