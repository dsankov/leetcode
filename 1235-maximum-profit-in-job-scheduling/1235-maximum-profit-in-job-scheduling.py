class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        max_end_time = max(endTime)
        sorted_start_time = [(start_time, idx) for idx, start_time in enumerate(startTime)]
        sorted_start_time.sort()
        original_start_indices = [idx for _, idx in sorted_start_time]
        sorted_start_time = [time for time, _ in sorted_start_time] 
        print(sorted_start_time, original_start_indices)
        dp = [-1] * n

        def max_profit(start_time_idx):
            if start_time_idx >= n:
                return 0
            if dp[start_time_idx] != -1:
                return dp[start_time_idx]

            start_time = sorted_start_time[start_time_idx]
            return 0



        return max_profit(sorted_start_time[0])
        # start_time_idx = [(start_time, idx) for idx, start_time in enumerate(startTime)]
        # index_to_time = {idx: time for time, idx in start_time_idx}
        # start_time_idx.sort()
        # # print(start_time_idx)

        # # def find_left(time_idx):
        # #     left = 0
        # #     right = n-1
        # #     while left < right:
        # #         mid = (right - left) // 2
        # #         if startTime[time_idx] == 

        # def max_profit(start_time_ptr):
            
        #     if start_time_ptr > n:
        #         return 0

        #     start_time = startTime[start_time_ptr]
        #     if dp[start_time] != -1:
        #         return dp[start_time]
                
        #     # next_jobs = set()
        #     use_next_job_profit = 0
        #     first_next_job_idx = bisect_left (start_time_idx, (start_time, -1))
        #     # print(first_next_job_idx)
        #     last_next_job_idx  = bisect_right(start_time_idx, (start_time, n+1))
        #     for next_job_idx in range(first_next_job_idx, last_next_job_idx):
        #         end_next_job_time = endTime[next_job_idx]
        #         use_next_job_profit = max(use_next_job_profit, max_profit(end_next_job_idx))

        #     skip_next_job_profit = 0
        #     first_next_job_idx = bisect_left (start_time_idx, (start_time + 1, -1))
        #     last_next_job_idx  = bisect_right(start_time_idx, (start_time + 1, n+1))
        #     for next_job_idx in range(first_next_job_idx, last_next_job_idx):
        #         end_next_job_time = endTime[next_job_idx]
        #         skip_next_job_profit = max(skip_next_job_profit, max_profit(end_next_job_idx))

        #     dp[start_time] = max(profit[start_time_ptr] + use_next_job_profit, skip_next_job_profit)
        #     return dp[start_time]

        # return max_profit(start_time_idx[0][1])


        