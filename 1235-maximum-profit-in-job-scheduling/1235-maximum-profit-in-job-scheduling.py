class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)
        jobs = sorted(zip(startTime, endTime, profit))

        max_gain_profit = 0
        end_time_profit_queue = []

        for curr_job_start_time, curr_job_end_time, curr_job_profit in jobs:
            while end_time_profit_queue:
                earlest_end_time, gain_profit = end_time_profit_queue[0]
                if curr_job_start_time < earlest_end_time:
                    break
                heappop(end_time_profit_queue)
                max_gain_profit = max(max_gain_profit, gain_profit) 
            heappush(end_time_profit_queue, (curr_job_end_time, curr_job_profit + max_gain_profit))



        return max(map(lambda item: item[1], end_time_profit_queue))