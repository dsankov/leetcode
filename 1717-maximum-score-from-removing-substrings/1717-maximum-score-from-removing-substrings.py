class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        x, y, more_gain_str = (x, y, "ab") if x >= y else (y, x, "ba")
        less_gain_str = more_gain_str[::-1]

        result = 0
        char_stack = deque()
        for char in s:
            if not char_stack:
                char_stack.append(char)
                continue
            if char != more_gain_str[1]:
                char_stack.append(char)
                continue
            if char_stack[-1] != more_gain_str[0]:
                char_stack.append(char)
                continue
            result += x
            char_stack.pop()

        s = char_stack
        char_stack = deque()
        for char in s:
            if not char_stack:
                char_stack.append(char)
                continue
            if char != less_gain_str[1]:
                char_stack.append(char)
                continue
            if char_stack[-1] != less_gain_str[0]:
                char_stack.append(char)
                continue
            result += y
            char_stack.pop()
        return result