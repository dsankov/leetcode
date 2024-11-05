class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def combination_sum(n_addendums: int, projected_sum: int, not_less_than: int = 1) -> list:
            if n_addendums == 1 and not_less_than <= projected_sum <= 9:
                return [[projected_sum]]

            min_possible_sum = n_addendums * (not_less_than - 1) + n_addendums * (n_addendums + 1) // 2
            max_possible_sum = 10 * n_addendums - n_addendums * (n_addendums + 1) // 2
            if min_possible_sum > projected_sum or max_possible_sum < projected_sum:
                return None

            results = []
            for first_addendum in range(not_less_than, 10):                
                sub_results = combination_sum(n_addendums - 1, projected_sum - first_addendum, first_addendum + 1)
                if sub_results:
                    for sub_result in sub_results:
                        sub_result.append(first_addendum)
                        results.append(sub_result)
            return results
        
        return combination_sum(k, n) or []
        