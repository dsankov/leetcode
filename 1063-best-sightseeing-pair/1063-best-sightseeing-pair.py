class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        max_score = values.copy()
        max_from_left = [-inf] * len(values)
        for i in range(1, n):
            max_from_left[i] = max(max_from_left[i-1] - 1, values[i-1] - 1)
        max_from_right = [-inf] * len(values)
        for i in range(n-2, -1, -1):
            max_from_right[i] = max(max_from_right[i+1] - 1, values[i+1] - 1)
        
        max_score = -inf
        return max(score + max(left_score, right_score) for left_score, score, right_score in zip(max_from_left, values, max_from_right))

 