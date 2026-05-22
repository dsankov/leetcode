class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if len(nums) == 1:
        #     return 0 if target == nums[0] else -1
        # while l < r:
        #     m = (l + r) // 2
        #     print(l,m, r)
        #     if nums[m] == target:
        #         return m
        #     if nums[m] < target:
        #         if target <= nums[r]:
        #             l = m + 1
        #         else:
        #             r = m
        #     elif target <= nums[m]:
        #         if nums[l] <= target:
        #             r = m
        #         else:
        #             l = m + 1
        # if nums[l] == target:
        #     return l
        # else:
        #     return -1
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            if l == r or nums[l] < nums[r]:
                shift = l
                break
            
            m = (l + r) // 2
            if nums[l] <= nums[m]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
        nums_ = nums[shift:]+nums[:shift]
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if target < nums_[m]:
                r = m
            elif nums_[m] < target:
                l = m + 1
            else:
                return (m + shift) % n
        return (l + shift) % n  if nums_[l] == target else -1

        