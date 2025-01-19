class Solution:
    def calculate(self, s: str) -> int:
        curr_sign = 1
        curr_num = 0
        curr_sub_result = 0
        sub_results_stack = []
        for char in s:
            if char == " ":
                continue
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
                continue

            curr_sub_result += curr_num * curr_sign
            curr_num = 0

            if char == "-":
                curr_sign = -1
                continue

            if char == "(":
                sub_results_stack.append(curr_sub_result)
                sub_results_stack.append(curr_sign)
                curr_sub_result = 0
                
            elif char == ")":
                prev_sign = sub_results_stack.pop()
                prev_sub_result = sub_results_stack.pop()
                curr_sub_result = prev_sub_result + curr_sub_result * prev_sign
                
            else: # "+"
                pass
            curr_sign = 1
        return curr_sub_result + curr_num * curr_sign


            

