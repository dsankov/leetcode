from pprint import pprint
class MinStack:

    def __init__(self):
        self.stack = deque()
        self.minimums = deque()
        self.minimums.append(inf)
        

    def push(self, val: int) -> None:
        self.minimums.append(min(val, self.minimums[-1]))
        self.stack.append(val)

        

    def pop(self) -> None:
        self.stack.pop()
        self.minimums.pop()

        

    def top(self) -> int:
       return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimums[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()