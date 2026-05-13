class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        costs = [0] * (2 * (limit + 1))
        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]
            if a > b:
                a, b = b, a
            
            costs[2] += 2
            costs[a + 1] -= 1
            costs[a + b] -= 1
            costs[a + b + 1] += 1
            costs[b + limit + 1] += 1
        min_cost = inf
        cur_cost = 0
        for to_value in range(2, 2 * (limit + 1)):
            cur_cost += costs[to_value]
            min_cost = min(min_cost, cur_cost)
        return min_cost

        