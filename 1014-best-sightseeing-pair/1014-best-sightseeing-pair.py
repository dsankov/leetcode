class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best_pair = 0
        answer = 0
        for sight in values:
            answer = max(answer, sight + best_pair)
            if sight > best_pair: 
                best_pair = sight - 1
            else: 
                best_pair -= 1
        return answer
# with open("user.out", "w") as f:
#     for nums in map(loads, stdin):
#         print(Solution().maxScoreSightseeingPair(nums),file=f)
# exit(0)
