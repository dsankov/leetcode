class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        groups_endtime_pq = []
        for interval_start, interval_end in sorted(intervals):
            if groups_endtime_pq and groups_endtime_pq[0] < interval_start:
                heappop(groups_endtime_pq)
            heappush(groups_endtime_pq, interval_end)

        return len(groups_endtime_pq)