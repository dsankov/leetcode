class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        arrivals = sorted((time[0], i) for i, time in enumerate(times))
        available_chairs = []
        next_free_chair = 0
        occupied_chairs = []
        for arrival_time, friend_id in arrivals:
            while occupied_chairs and occupied_chairs[0][0] <= arrival_time:
                _free_time, chair = heappop(occupied_chairs)
                heappush(available_chairs, chair)
            if not available_chairs:
                next_chair = next_free_chair
                next_free_chair += 1
            else:
                next_chair = heappop(available_chairs)
            if friend_id == targetFriend:
                return next_chair
            heappush(occupied_chairs,(times[friend_id][1], next_chair))
        
        return 0