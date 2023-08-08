class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:

        
        left, right = 0, len(nums)-1
        sum_of_nums = sum(nums)
        map_not_poss = {}

        def can_split(left, right, sum_of_nums):
            if right-left <= 1:
                return True
            if (left,right) in map_not_poss:
                return False

            result = False

            if sum_of_nums - nums[left] >= m:
                result = can_split(left+1, right, sum_of_nums - nums[left])
            if result:
                return result

            if sum_of_nums - nums[right] >= m:
                result = can_split(left, right-1, sum_of_nums - nums[right])
            if result:
                return result

            map_not_poss[(left,right)] = False
            return False

        return can_split(left, right, sum_of_nums)
            
        