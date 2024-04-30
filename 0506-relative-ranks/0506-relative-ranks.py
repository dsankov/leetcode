class Solution:
    def findRelativeRanks(self, scores: List[int]) -> List[str]:
        def position_to_str(n: int) -> str:
            PEDESTAL = ["Gold Medal","Silver Medal","Bronze Medal"]
            if n < 3:
                return PEDESTAL[n]
            return str(n+1)
        
        n = len(scores)
        sorted_indexed_scores = sorted(zip(scores, range(n)), key=lambda score: score[0], reverse=True)
        result = [""] * n
        
        for position, (score, index) in enumerate(sorted_indexed_scores):
            result[index] = position_to_str(position)
            
        return result