class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiants = deque()
        dires = deque()
        for position, member in enumerate(senate):
            if member == "R":
                radiants.append(position)
            else:
                dires.append(position)
        while radiants and dires:
            radiant = radiants.popleft()
            dire = dires.popleft()
            position += 1
            if radiant < dire:
                radiants.append(position)
            else:
                dires.append(position)
        if radiants:
            return "Radiant"
        else:
            return "Dire"
