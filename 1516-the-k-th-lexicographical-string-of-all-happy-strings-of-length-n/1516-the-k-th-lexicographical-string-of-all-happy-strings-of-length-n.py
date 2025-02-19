class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_str_num = 3 * 2**(n-1)
        if k > happy_str_num:
            return ""
        

        result = ["a"] * n
        next_smallest = {
            "a": "b",
            "b": "a",
            "c": "a",
            }
        next_greatest = {
            "a": "c",
            "b": "c",
            "c": "b",
        }
        start_a = 1
        start_b = start_a + 2**(n-1)
        start_c = start_b + 2**(n-1)
        if k < start_b:
            result[0] = "a"
            k -= start_a
        elif k < start_c:
            result[0] = "b"
            k -= start_b
        else:
            result[0] = "c"
            k -= start_c

        for char_idx in range(1, n):
            mid_point = 2 ** (n-1 - char_idx)
            if k < mid_point:
                result[char_idx] = next_smallest[
                    result[char_idx-1]
                    ]
            else:
                result[char_idx] = next_greatest[result[char_idx-1]]
                k -= mid_point

        return "".join(result)
