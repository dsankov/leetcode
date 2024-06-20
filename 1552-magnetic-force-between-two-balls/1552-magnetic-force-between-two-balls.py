class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def can_place_with_distance(distance: int) -> bool:
            previous_used_basket = position[0]
            used_balls = 1
            for basket in position:
                if basket - previous_used_basket >= distance:
                    used_balls += 1
                    previous_used_basket = basket
                if used_balls == m:
                    return True
            return False
        
        position.sort()
        left = 1
        right = (position[-1] - position[0]) // (m - 1)
        result = 0
        while left <= right:
            middle = left + (right-left) // 2
            if can_place_with_distance(middle):
                result = middle
                left = middle + 1
            else:
                right = middle - 1
        
        return result
                