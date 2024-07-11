class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair_parentheses_for = [1] * n
        parentheses_stack = deque()
        for i, char in enumerate(s):
            if char == "(":
                parentheses_stack.append(i)
            elif char == ")":
                pair_parentheses = parentheses_stack.pop()
                pair_parentheses_for[i] = pair_parentheses
                pair_parentheses_for[pair_parentheses] = i
        i = 0
        direction = 1
        result = []
        while i < n:
            if s[i] in "()":
                direction *= -1
                i = pair_parentheses_for[i]
            else:
                result.append(s[i])
            i += direction

        return "".join(result)