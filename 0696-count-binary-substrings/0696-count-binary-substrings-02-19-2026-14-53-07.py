class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        result = 0
        n = len(s)
        prev_segment_len = 0
        cur_segment_len = 1

        for i in range(1, n):
            if s[i] == s[i-1]:
                cur_segment_len += 1
                if cur_segment_len <= prev_segment_len:
                    result += 1

            else:
                result += 1
                prev_segment_len = cur_segment_len
                cur_segment_len = 1
       
       
       
       
       
       
        # for a, b in pairwise(s):
        #     print(f"{a=} {b=} {prev_segment_len=} {cur_segment_len=} {result=}")
        #     if a == b:
        #         cur_segment_len += 1
        #         result += min(prev_segment_len, cur_segment_len)
        #     else:
        #         prev_segment_len = cur_segment_len
        #         cur_segment_len = 1
        #         result += 1
        #     print(f"Update result: {result}")
        return result
