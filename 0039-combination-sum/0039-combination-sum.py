class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        result = []
        sub_result = []

        def dfs(candidate_index, target):
            if candidate_index >= n or candidates[candidate_index] > target:
                return
            if candidates[candidate_index] == target:
                result.append(sub_result + [candidates[candidate_index]])
                return

            sub_result.append(candidates[candidate_index])
            dfs(candidate_index, target - candidates[candidate_index])
            sub_result.pop()
            dfs(candidate_index + 1, target)

        dfs(0, target)
        return result

            

        