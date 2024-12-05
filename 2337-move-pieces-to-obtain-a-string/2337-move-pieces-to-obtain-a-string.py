class Solution:
    def canChange(self, start: str, target: str) -> bool:

        start_queue = deque()
        target_queue = deque()
        for i, (p1, p2) in enumerate(zip(start, target)):
            if p1 != "_":
                start_queue.append((i, p1))
            if p2 != "_":
                target_queue.append((i, p2))

        if len(start_queue) != len(target_queue):
            return False
        while start_queue:
            i1, p1 = start_queue.popleft()
            i2, p2 = target_queue.popleft()
            if p1 != p2:
                return False
            if (p1 == "R" and i1 > i2
                or p1 == "L" and i1 < i2
            ):
                    return False


        

        return True
