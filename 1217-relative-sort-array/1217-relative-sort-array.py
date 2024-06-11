class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:  
        counted_nums = Counter(arr1)
        result = []
        for num in arr2:
            result.extend([num]*counted_nums[num])
            counted_nums[num] = 0
            
        tail = sorted([num for num in counted_nums if counted_nums[num] > 0 ])
        for num in tail:
            result.extend([num]*counted_nums[num])
        return result
    