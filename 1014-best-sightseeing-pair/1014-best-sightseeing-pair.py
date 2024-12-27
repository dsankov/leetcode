class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_prev = values[0]
        max_score = 0
        for value in values[1:]:
            max_score = max(max_score, value + max_prev- 1)
            max_prev = max(max_prev - 1, value)
        return max_score
        