class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        nums_queue = [(num, index) for index, num in enumerate(nums)]
        heapify(nums_queue)
        total_score = 0
        marked_indices = [False] * n
        while nums_queue:
            min_num, idx = heappop(nums_queue)
            if marked_indices[idx]:
                continue
            total_score += min_num
            marked_indices[idx] = True
            for adj_idx in [idx-1, idx+1]:
                if 0 <= adj_idx < n:
                    marked_indices[adj_idx] = True
        return total_score
            
        