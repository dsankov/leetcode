class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = deque()
        keys.extend(rooms[0])
        opened_rooms = set()
        opened_rooms.add(0)
        
        while keys:
            key = keys.pop()
            if key in opened_rooms:
                continue
            opened_rooms.add(key)
            keys.extend(rooms[key])

        return len(opened_rooms) == len(rooms)