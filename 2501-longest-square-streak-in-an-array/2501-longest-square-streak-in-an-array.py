class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = set(nums)
        max_streak = 0
        
        for num in nums:
            current_streak = 1
            squared_num = num * num
            while squared_num in nums:
                current_streak += 1
                squared_num *= squared_num

            max_streak = max(max_streak, current_streak)

        return max_streak if max_streak >= 2 else -1


        