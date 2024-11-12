class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands_stack = []
        for token in tokens:
            if token[0].isdigit() or len(token) > 1 and token[0] == "-":
                operands_stack.append(int(token))
            else:
                operand2 = operands_stack.pop()
                operand1 = operands_stack.pop()
                match token:
                    case "+":
                        sub_result = operand1 + operand2
                    case "-":
                        sub_result = operand1 - operand2
                    case "*":
                        sub_result = operand1 * operand2
                    case "/":
                        sub_result = int(operand1 / operand2)
                operands_stack.append(sub_result)        

        return operands_stack.pop()
        