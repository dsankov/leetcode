class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def finish_time(starts, durations, treshold):
            min_finish = inf
            for start, duration in zip(starts, durations):
                if start < treshold:
                    start = treshold
                min_finish = min(min_finish, start + duration)
            return min_finish
        
        return min(
            finish_time(landStartTime, landDuration, finish_time(waterStartTime, waterDuration, 0)),
            finish_time(waterStartTime, waterDuration, finish_time(landStartTime, landDuration, 0)
            )
        )