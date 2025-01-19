class Solution:
    def calculate(self, s: str) -> int:
        self.s = list(char for char in s if char !=" ")
        self.n = len(self.s)
        self.ptr = 0
        return self.eval_expr()

    def eval_expr(self):
        result = 0
        if self.s[self.ptr] == "(":
            self.ptr += 1
            result += self.eval_expr()
            self.ptr += 1
        elif self.s[self.ptr] == "-":
            self.ptr += 1
            if self.s[self.ptr] == "(":
                self.ptr += 1
                result -= self.eval_expr()
                self.ptr += 1
            else:
                result -= self.get_num()
        else:
            result = self.get_num()

        while self.ptr < self.n and self.s[self.ptr] in "+-":
            operation = self.s[self.ptr]
            self.ptr += 1
            if self.s[self.ptr] == "(":
                self.ptr += 1
                next_operand = self.eval_expr()
                self.ptr += 1
            else:
                next_operand = self.get_num()

            if operation == "+":
                result = result + next_operand
            elif operation == "-":
                result = result - next_operand
        return result

    def get_num(self):
        num = int(self.s[self.ptr])
        self.ptr += 1
        while self.ptr < self.n and self.s[self.ptr].isdigit():
            num = num * 10 + int(self.s[self.ptr])
            self.ptr += 1
        return num


