class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        prev_symbol = {"B": "A", "D": "C"}
        for char in s:
            if char in "BD":
                if stack and stack[-1] == prev_symbol[char]:
                    stack.pop()
                    continue
            stack.append(char)
        return len(stack)
        