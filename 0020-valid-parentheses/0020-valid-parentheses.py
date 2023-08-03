
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_bracket_for = {
            ']' : '[',
            ')' : '(',
            '}' : '{',
            }
        
        for symbol in s:


            if symbol in "[({":
                stack.append(symbol)
            elif symbol in "])}":
                if not stack:
                    return False

                if stack[-1] == opening_bracket_for[symbol]:

                    stack.pop()
                else:
                    return False
            else:
                return False
        return len(stack) == 0
