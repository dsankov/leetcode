class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        START, END = 0, 1
        events = []
        for balloon_index, (start_point, end_point) in enumerate(points):
            events.append((start_point, START, balloon_index))
            events.append((end_point, END, balloon_index))
        events.sort()
        targeted = set()
        bursted = set()
        num_arrows = 0
        for event_point, event_type, balloon_index in events:
            if event_type == START:
                targeted.add(balloon_index)
            elif balloon_index not in bursted:
                num_arrows += 1
                bursted |= targeted
                targeted = set()

        return num_arrows
        