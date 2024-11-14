class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        START, END = range(2)
        events = []
        for interval_start, interval_end in intervals:
            events.append((interval_start, START))
            events.append((interval_end, END))
        events.sort()
        result = []
        depth = 0
        for point, event_type in events:
            if event_type == START:
                depth += 1
                if depth == 1:
                    curr_start = point
            if event_type == END:
                depth -= 1
                if depth == 0:
                    curr_end = point
                    if result and result[-1][1] == curr_start:
                        result[-1][1] = curr_end
                    else:
                        result.append([curr_start, curr_end])

        return result
            
        