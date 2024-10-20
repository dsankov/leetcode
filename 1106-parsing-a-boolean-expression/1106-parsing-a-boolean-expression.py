class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        expression_stack = deque()
        for curr_char in expression:
            if curr_char == "t":
                expression_stack.append(True)
            elif curr_char == "f":
                expression_stack.append(False)
            elif curr_char in "!|&":
                expression_stack.append(curr_char)
            elif curr_char == ")":
                has_true = False
                has_false = False
                while expression_stack[-1] in (True, False):
                    value = expression_stack.pop()
                    has_true |= value
                    has_false |= not value
                operation = expression_stack.pop()
                if operation == "!":
                    expression_stack.append(not has_true)
                elif operation == "|":
                    expression_stack.append(has_true)
                elif operation == "&":
                    expression_stack.append(not has_false)

        return expression_stack[-1]