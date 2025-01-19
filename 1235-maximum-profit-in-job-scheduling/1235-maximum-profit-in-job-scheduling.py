class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)
        jobs = [(start_time, end_time, job_profit) for start_time, end_time, job_profit in zip(startTime, endTime, profit)]
        jobs.sort()
        max_profit = [-1] * n

        def get_max_profit(job_start_idx):
            if job_start_idx >= n:
                return 0
            if max_profit[job_start_idx] != -1:
                return max_profit[job_start_idx]

            def first_availible_job(job_start_idx, job_start_time):
                left, right = job_start_idx, n-1
                availible_job_idx = -1
                while left <= right:
                    mid = (left + right) // 2
                    mid_start_time, mid_end_time, mid_profit = jobs[mid]
                    if mid_start_time >= job_start_time:
                        availible_job_idx = mid
                        right = mid - 1
                    else:
                        left = mid + 1
                return availible_job_idx

            curr_job_start_time, curr_job_end_time, curr_job_profit = jobs[job_start_idx]
            next_availible_use_job_idx = first_availible_job(job_start_idx=job_start_idx+1, job_start_time=curr_job_end_time)
            if next_availible_use_job_idx == -1:
                 max_use_job_profit = curr_job_profit
            else:
                max_use_job_profit = (curr_job_profit 
                                    + get_max_profit(job_start_idx=next_availible_use_job_idx)
                )
            
            next_availible_skip_job_idx = first_availible_job(job_start_idx=job_start_idx+1, job_start_time=curr_job_start_time)
            if next_availible_skip_job_idx == -1:
                max_skip_job_profit = 0
            else:
                max_skip_job_profit = get_max_profit(job_start_idx=next_availible_skip_job_idx)

            max_profit[job_start_idx] = max(max_use_job_profit, max_skip_job_profit)
            return max_profit[job_start_idx]


        return get_max_profit(job_start_idx=0)