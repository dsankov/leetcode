class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        total_waiting_time = 0
        finish_job_time = 0
        for arrival, time in customers:
            if finish_job_time <= arrival:
                finish_job_time = arrival + time
                total_waiting_time += time
            else:
                finish_job_time += time
                total_waiting_time += (finish_job_time - arrival)
        return total_waiting_time / n