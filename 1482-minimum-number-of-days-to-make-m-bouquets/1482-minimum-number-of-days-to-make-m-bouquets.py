class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def bouquets_enough(test_day: int) -> bool:
            num_bouquets = 0
            flower_line = 0
            for day in bloomDay:
                if day <= test_day:
                    flower_line += 1
                else:
                    flower_line = 0
                if flower_line == k:
                    num_bouquets += 1
                    flower_line = 0
            return num_bouquets >= m

        if len(bloomDay) < m * k:
            return -1

        left = 1
        right = max(bloomDay)
        while left < right:
            middle = (left + right) // 2
            if bouquets_enough(middle):
                right = middle
            else:
                left = middle + 1

        return right