class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        max_candies_in_pile = max(candies)
        def can_allocate_k_candies(k_candies: int) -> bool:
            max_num_of_children = 0
            for pile in candies:
                max_num_of_children += pile // k_candies
            return max_num_of_children >= k 
        
        left = 0
        right = max_candies_in_pile

        while left < right:
            middle = (left + right + 1) // 2
            if can_allocate_k_candies(middle):
                left = middle
            else:
                right = middle - 1

        return left
        