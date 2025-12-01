class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        live = batteries[ -n : ]
        extra= sum(batteries[ : -n ])

        for i in range(n - 1):
            upgrade_step = live[i + 1] - live[i]
            upgrade_count = i + 1
            upgrade_amount = upgrade_step * upgrade_count 
            if upgrade_amount <= extra:
                extra -= upgrade_amount
            else:
                return live[i] + extra // (upgrade_count)

        return live[-1] + extra // n
        