class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks = sorted(tasks, key=lambda task: task[0] - task[1])
        init_amount = 0
        deposit = 0
        for (a, m) in tasks:
            d = m - a
            if deposit < m:
                init_amount += m - deposit
                deposit = m
            deposit -= a

        return init_amount
        