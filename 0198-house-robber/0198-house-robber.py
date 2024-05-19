class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n <= 2:
            return(max(nums))
        
        with_house = [0] * n
        without_house = [0] * n
        with_house[0] = nums[0]
        without_house[0] = 0
        with_house[1] = nums[1]
        without_house[1] = nums[0]
        
        for i in range(2, n):
            with_house[i] = max(nums[i] + with_house[i-2],
                                nums[i] + without_house[i-1])
            without_house[i] = max(with_house[i-1],
                                with_house[i-2],
                                without_house[i-2])
        return max(with_house[n-1], without_house[n-1])
            
        