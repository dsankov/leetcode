class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        right = 0
        zeroes= 0
        max_len = 0
        cur_len = 0
        

        while right < n:
            if nums[right] == 1:
                cur_len += 1
                right += 1
            else:
                if zeroes < k:
                    cur_len += 1
                    zeroes += 1
                    right += 1
                else:
                    if nums[left] == 0:
                        zeroes =  max(0, zeroes-1)
                    cur_len = max(0, cur_len-1)
                    left += 1
                    right = max(right, left)
            max_len = max(max_len, cur_len)

        return max_len
