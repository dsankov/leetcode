class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n
        idx_queue = deque()
        idx_queue.append(start)

        while idx_queue:
            cur_idx = idx_queue.popleft()
            if visited[cur_idx]:
                continue
            if arr[cur_idx] == 0:
                return True
            visited[cur_idx] = True
            if cur_idx - arr[cur_idx] >= 0:
                idx_queue.append(cur_idx - arr[cur_idx])
            if cur_idx + arr[cur_idx] < n:
                idx_queue.append(cur_idx + arr[cur_idx])
        return False