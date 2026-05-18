class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        jump_groups = defaultdict(set)
        for idx, num in enumerate(arr):
            jump_groups[num].add(idx)

        num_jumps = -1
        idx_queue = deque([0])
        seen_nums = set()
        while idx_queue:
            level_len = len(idx_queue)
            num_jumps += 1
            for _ in range(level_len):
                cur_idx = idx_queue.popleft()
                if cur_idx == n - 1:
                    return num_jumps
                cur_num = arr[cur_idx]
                if cur_num not in seen_nums:
                    seen_nums.add(cur_num)
                    idx_queue.extend(list(jump_groups[cur_num] - {cur_idx}))
                for adj_idx in [cur_idx - 1, cur_idx + 1]:
                    if 0 <= adj_idx < n and arr[adj_idx] not in seen_nums:
                        idx_queue.append(adj_idx)



        return num_jumps
        