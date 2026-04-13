class MyStack:

    def __init__(self):
        self.in_queue = deque()
        self.out_queue = deque()
        

    def push(self, x: int) -> None:
        self.in_queue.append(x)
        

    def pop(self) -> int:
        while len(self.in_queue) > 1:
                self.out_queue.append(self.in_queue.popleft())
        self.in_queue, self.out_queue = self.out_queue, self.in_queue 
        return self.out_queue.popleft()
        

    def top(self) -> int:
        while len(self.in_queue) > 1:
                self.out_queue.append(self.in_queue.popleft())
        top_val = self.in_queue[0]
        self.out_queue.append(self.in_queue.popleft())
        self.in_queue, self.out_queue = self.out_queue, self.in_queue 
        return top_val
        

    def empty(self) -> bool:
        return not (self.in_queue)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()