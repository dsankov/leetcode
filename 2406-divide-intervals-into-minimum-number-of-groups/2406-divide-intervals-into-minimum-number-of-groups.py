class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        for interval_start, interval_end in intervals:
            events.append((interval_start, 1))
            events.append((interval_end + 1, -1))
        events.sort()
        max_interseptions = 0
        current_interseptions = 0
        for event_time, event_type in events:
            current_interseptions += event_type
            max_interseptions = max(max_interseptions, current_interseptions)
        return max_interseptions