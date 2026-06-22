class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        max_len = 0
        seen_deltas = {0: -1}
        cur_delta = 0
        for pos, num in enumerate(nums):
            cur_delta += 2 * num - 1 

            if cur_delta in seen_deltas:
                max_len = max(max_len, pos - seen_deltas[cur_delta])
            else:
                seen_deltas[cur_delta] = pos



        return max_len