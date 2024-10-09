class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        unbalanced_open_brackets = 0
        unbalanced_close_brackets = 0
        for char in s:
            if char == ")":
                if unbalanced_open_brackets == 0:
                    unbalanced_close_brackets += 1
                else:
                    unbalanced_open_brackets -= 1
            else:
                unbalanced_open_brackets += 1
        return unbalanced_open_brackets + unbalanced_close_brackets
        