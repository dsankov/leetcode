class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:        
        
        numbers_to_sum = []
        max_sum = sum(numbers_to_sum) # == 0
        result = 0
        sorted_pairs = sorted(zip(nums1, nums2), key=lambda pair: pair[1], reverse=True)
        
        for n1, n2 in sorted_pairs:
            heapq.heappush(numbers_to_sum, n1)
            max_sum += n1
                
            if len(numbers_to_sum) == k:
                result = max(result, max_sum * n2)
                max_sum -= heapq.heappop(numbers_to_sum)
             
        return result