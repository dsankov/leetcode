class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 1:
            return nums
        left = 0
        right = 1
        strike = 1
        result = []
        while right < n:
            
            if nums[right] == nums[right - 1] + 1:
                strike += 1
            else:
                strike = 1

            if right < k-1:
                right += 1
                continue

            if strike >= k:
                result.append(nums[right])
                if nums[left] == nums[left+1]:
                    strike -= 1 
            else:
                result.append(-1)

            
            right += 1
            left += 1
        return result