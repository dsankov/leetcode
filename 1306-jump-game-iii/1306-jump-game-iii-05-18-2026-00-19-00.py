class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n
        idx_stack = deque([start])
        visited[start] = True

        while idx_stack:
            cur_idx = idx_stack.popleft()
            if arr[cur_idx] == 0:
                return True

            left, right = cur_idx - arr[cur_idx], cur_idx + arr[cur_idx]
            if left >= 0 and not visited[left]:
                idx_stack.append(cur_idx - arr[cur_idx])
                visited[left] = True
            if right < n and not visited[right]:
                idx_stack.append(right)
                visited[right] = True
        return False