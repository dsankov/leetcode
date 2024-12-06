class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        curr_sum = 0
        result = 0
        for num in range(1, n + 1):
            if curr_sum + num > maxSum:
                break
            if num not in banned: 
                result += 1
                curr_sum += num
        return result
            