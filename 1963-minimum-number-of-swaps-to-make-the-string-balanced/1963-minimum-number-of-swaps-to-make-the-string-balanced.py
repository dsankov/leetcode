class Solution:
    def minSwaps(self, s: str) -> int:
        unbalanced_open_brackets = 0
        unbalanced_close_brackets = 0
        for char in s:
            if char == "]":
                if unbalanced_open_brackets == 0:
                    unbalanced_close_brackets += 1
                else:
                    unbalanced_open_brackets -= 1
            else:
                unbalanced_open_brackets += 1
        assert unbalanced_open_brackets == unbalanced_close_brackets
        return (unbalanced_open_brackets + 1) // 2

        