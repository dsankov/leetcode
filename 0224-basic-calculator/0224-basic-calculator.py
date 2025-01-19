class Solution:
    def calculate(self, s: str) -> int:
        self.s = list(char for char in s if char !=" ")
        self.n = len(self.s)
        self.ptr = 0
        self.level = 0
        return self.eval_expr(level=0)

    def eval_expr(self, level):
        indent = "\t" * level
        # print(f"{indent}expr_start={self.ptr}->{self.s[self.ptr]}")
        result = 0
        if self.s[self.ptr] == "(":
            self.ptr += 1
            result += self.eval_expr(level+1)
            # if self.s[self.ptr] != ")":
                # print("!!!")
            self.ptr += 1

        elif self.s[self.ptr] == "-":
            self.ptr += 1
            if self.s[self.ptr] == "(":
                self.ptr += 1
                result -= self.eval_expr(level+1)
                # if self.s[self.ptr] != ")":
                    # print("!!!")
                self.ptr += 1
            else:
                result -= self.get_num()
        else:
            result = self.get_num()

        # print(f"{indent}{result=}")
        while self.ptr < self.n and self.s[self.ptr] in "+-":
            operation = self.s[self.ptr]
            # print(f"{indent}{operation=}")

            self.ptr += 1
            if self.s[self.ptr] == "(":
                self.ptr += 1
                next_operand = self.eval_expr(level+1)
                # if self.s[self.ptr] != ")":
                    # print("!!!")
                self.ptr += 1
            else:
                next_operand = self.get_num()

            if operation == "+":
                result = result + next_operand
            elif operation == "-":
                result = result - next_operand
            # print(f"{indent}{next_operand=} {result=}")

        # if self.ptr >= self.n:
        #     # print(f"{indent}!!! expr_end={self.ptr}")
        # else:
            # print(f"{indent}expr_end={self.ptr}->{self.s[self.ptr]}")

        return result

    def get_num(self):
        num = int(self.s[self.ptr])
        self.ptr += 1
        while self.ptr < self.n and self.s[self.ptr].isdigit():
            num = num * 10 + int(self.s[self.ptr])
            self.ptr += 1
        return num





        # def eval_expr():
        #     print(f"{self.ptr} -> {self.s[self.ptr]}")
        #     if self.ptr >= self.n:
        #         return 0

        #     def get_num():
        #         num = int(self.s[self.ptr])
        #         self.ptr += 1
        #         while self.ptr < self.n and self.s[self.ptr].isdigit():
        #             num = num * 10 + int(self.s[self.ptr])
        #             self.ptr += 1
        #         return num


        #     if self.s[self.ptr] == "(":
        #         self.ptr += 1
        #         result = eval_expr()
        #         self.ptr += 1

        #     elif self.s[self.ptr] == "-":
        #         self.ptr += 1
        #         if self.s[self.ptr] == "(":
        #             self.ptr += 1
        #             result = - eval_expr()
        #             self.ptr += 1
        #         else:
        #             result = - get_num()
        #     else:
        #         result = get_num()

        #     while self.ptr < self.n:
        #         if self.s[self.ptr] == ")":
        #             # self.ptr += 1
        #             return result

        #         operation = self.s[self.ptr]
        #         print(f"{operation=}")
        #         self.ptr += 1
        #         if self.s[self.ptr].isdigit():
        #             next_operand = get_num()
        #         else:
        #             next_operand = eval_expr()
                
        #         if operation == "+":
        #             result = result + next_operand
        #         elif operation == "-":
        #             result = result - next_operand
        #     return result

        # return eval_expr()
        