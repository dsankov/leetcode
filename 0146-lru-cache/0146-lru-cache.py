class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_cache = {}
        self.last_key_usage = [-1] * (10**4 + 1)
        self.usage_deque = deque()
        self.op_id = 0

        

    def get(self, key: int) -> int:
        if self.last_key_usage[key] != -1:
            self.usage_deque.appendleft((self.op_id, key))
            self.last_key_usage[key] = self.op_id
            self.op_id += 1
            return self.lru_cache[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if self.last_key_usage[key] != -1:
            self.lru_cache[key] = value
            self.usage_deque.appendleft((self.op_id, key))
            self.last_key_usage[key] = self.op_id
            self.op_id += 1
            return
        self.lru_cache[key] = value
        self.usage_deque.appendleft((self.op_id, key))
        self.last_key_usage[key] = self.op_id
        
        while len(self.lru_cache) > self.capacity:
            oldest_op_id, oldest_used_key = self.usage_deque.pop()
            if self.last_key_usage[oldest_used_key] != oldest_op_id:
                continue
            self.last_key_usage[oldest_used_key] = -1
            if oldest_used_key in self.lru_cache:
                del self.lru_cache[oldest_used_key]
            
        self.op_id += 1

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)