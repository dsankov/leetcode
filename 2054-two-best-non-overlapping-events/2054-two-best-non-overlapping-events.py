class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        END, START = range(2)
        times = []
        for event_start, event_end, event_value in events:
            times.append((event_start, START, event_value))
            times.append((event_end + 1, END, event_value))
        times.sort()
        max_passed_event_value = 0
        max_sum_of_2_events = 0
        for time, event_type, event_value in times:
            if event_type == END:
                max_passed_event_value = max(max_passed_event_value, event_value)
            else:
                max_sum_of_2_events = max(max_sum_of_2_events, max_passed_event_value + event_value)
        return max_sum_of_2_events