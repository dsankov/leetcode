class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = deque()
        self.max_size = maxSize
        

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append([x, 0])
        

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1

        value, increment = self.stack.pop()
        if len(self.stack) > 0:
            self.stack[-1][1] += increment
        return value + increment
        

    def increment(self, k: int, val: int) -> None:
        if len(self.stack) > 0 and k > 0:
            self.stack[min(k-1, len(self.stack)-1)][1] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)