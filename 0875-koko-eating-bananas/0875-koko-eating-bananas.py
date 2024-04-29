class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check_eating_speed(k: int) -> bool:
            time = 0
            
#            for pile in piles:
#                time += pile // k
#                time += 1 if pile % k else 0
            
            for pile in piles:
                time += math.ceil(pile / k)
            return time <= h
        
        left, right = 1, max(piles)
        if len(piles) > h:
            return -1
        
        while left < right:
            medium = (left + right) // 2
            
#            if check_eating_speed(medium):                
            time = 0            
            for pile in piles:
                time += pile // medium
                time += 1 if pile % medium else 0
            
#            for pile in piles:
#                time += math.ceil(pile / medium)
            
            if time <= h:
                right = medium
            else:
                left = medium + 1
                
        return left