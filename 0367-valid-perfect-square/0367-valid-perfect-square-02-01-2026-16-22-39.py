class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        left, right = 1, num
        while left <= right:
            mid = left + (right - left) // 2
            mid2 = mid * mid
            if mid2 == num:
                return True
            if mid2 > num:
                right = mid - 1
            else:
                left = mid + 1
        return False