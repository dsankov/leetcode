from collections import deque

class MyQueue:

    def __init__(self):
        self.write_buffer = deque()
        self.read_buffer = deque()
    
    def _transfere_buffers(self):
        while self.write_buffer:
            self.read_buffer.append(self.write_buffer.pop())
        

    def push(self, x: int) -> None:
        self.write_buffer.append(x)
        

    def pop(self) -> int:
        if self.read_buffer:
            return self.read_buffer.pop()
        
        self._transfere_buffers()
        return self.read_buffer.pop()
        

    def peek(self) -> int:
        value = self.pop()
        self.read_buffer.append(value)
        return value
        

    def empty(self) -> bool:
        return not self.write_buffer and not self.read_buffer
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()