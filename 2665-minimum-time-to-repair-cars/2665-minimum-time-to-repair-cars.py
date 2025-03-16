class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        rank_counts = Counter(ranks)
        left_time = 1
        right_time = cars ** 2 * min(rank_counts)
        while left_time < right_time:
            mid_time = (left_time + right_time) // 2
            repaired_cars = sum(
                int((mid_time / rank) ** 0.5) * count
                for rank, count in rank_counts.items()
            )
            if repaired_cars < cars:
                left_time = mid_time + 1
            else:
                right_time = mid_time

        return left_time
        