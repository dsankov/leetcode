class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        class Strenght:
            def __init__(self, position, strenght) -> None:
                self.position = position
                self.strenght = strenght
                
            def __lt__(self, other):
                if self.strenght < other.strenght:
                    return True
                elif self.strenght == other.strenght and self.position < other.position:
                    return True       
                return False
            
        n = len(mat)
        
        strenghts = [(sum(mat[i]), i) for i in range(n)]
        heapq.heapify(strenghts)
   
        result = [strenght[1] for strenght in heapq.nsmallest(k, strenghts)]
        return result
        
        
#         strenghts = [Strenght(i, sum(mat[i])) for i in range(n)]
#         heapq.heapify(strenghts)
   
#         result = [strenght.position for strenght in heapq.nsmallest(k, strenghts)]
#         # for i in range(k):
#         #     strenght = heapq.heappop(strenghts)
#         #     result.append(strenght.position)
#         return result