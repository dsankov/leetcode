class Node:
    def __init__(self, freq):
        self.freq = freq
        self.prev = None
        self.next = None
        self.keys = set()

class AllOne:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

        
    def inc(self, key: str) -> None:
        if key not in self.map:
            first_node = self.head.next
            if first_node == self.tail or first_node.freq != 1:
                new_node = Node(1)
                new_node.keys.add(key)
                self.map[key] = new_node

                new_node.next = first_node
                first_node.prev = new_node
                new_node.prev = self.head
                self.head.next = new_node
            else:
                first_node.keys.add(key)
                self.map[key] = first_node
            
        else: # key is in self.map
            node = self.map[key]
            freq = node.freq
            node.keys.remove(key)

            next_node = node.next
            if next_node == self.tail or next_node.freq != freq + 1:
                new_node = Node(freq + 1)
                new_node.keys.add(key)
                self.map[key] = new_node
                new_node.next = next_node
                next_node.prev = new_node
                new_node.prev = node
                node.next = new_node
            else:
                next_node.keys.add(key)
                self.map[key] = next_node

            if not node.keys:
                self._remove_node(node)

    def dec(self, key: str) -> None:
        if key not in self.map:
            return
        node = self.map[key]
        freq = node.freq
        node.keys.remove(key)

        if  freq == 1:
            del self.map[key]
        else:
            prev_node = node.prev
            if prev_node == self.head or prev_node.freq != freq - 1:
                new_node = Node(freq - 1)
                new_node.keys.add(key)
                self.map[key] = new_node
                new_node.prev = prev_node
                prev_node.next = new_node
                new_node.next = node
                node.prev = new_node
            else:
                prev_node.keys.add(key)
                self.map[key] = prev_node

        if not node.keys:
            self._remove_node(node)
     

    def getMaxKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.tail.prev.keys))
        

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))

    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()