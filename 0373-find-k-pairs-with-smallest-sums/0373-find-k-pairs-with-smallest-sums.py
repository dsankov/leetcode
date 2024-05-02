class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n, m = len(nums1), len(nums2)
        if n == 0:
            return None
        
        visited_pairs = set()
        
        pairs_heap = []
        pairs_heap.append((nums1[0]+nums2[0], 0 ,0))
        result = []
        while len(result) < k:
            pair_sum, y, x = heappop(pairs_heap)
            if (y, x) in visited_pairs:
                continue
            visited_pairs.add((y, x))
            result.append([nums1[y], nums2[x]])
            if y + 1 < n:
                heappush(pairs_heap, (nums1[y+1] + nums2[x], y + 1, x))
            if x + 1 < m:
                heappush(pairs_heap, (nums1[y] + nums2[x+1], y, x + 1))

        return result
        
        