class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        n = len(workerTimes)
        total_times = sum(workerTimes)
        def check_time(time: int) -> bool:
            total_reduce = 0
            for worker_time in workerTimes:
                worker_amount = int((sqrt(1+8*time/worker_time) - 1) / 2)
                total_reduce += worker_amount

            return total_reduce >= mountainHeight

        min_time = 0
        max_time = max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2

        while min_time < max_time:
            med_time = (min_time + max_time) // 2
            # print(min_time, med_time, max_time)

            if check_time(med_time):
                max_time = med_time
            else:
                min_time = med_time + 1

        return max_time
        
        