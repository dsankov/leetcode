class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = list(range(n))
        robots.sort(key=lambda i: positions[i])
        robot_stack = deque()
        for robot in robots:
            if directions[robot] == "R":
                robot_stack.append(robot)
            else:
                while robot_stack and healths[robot] > 0:
                    combatant = robot_stack.pop()
                    if healths[combatant] > healths[robot]:
                        healths[combatant] -= 1
                        healths[robot] = 0
                        robot_stack.append(combatant)
                    elif healths[combatant] < healths[robot]:
                        healths[robot] -= 1
                        healths[combatant] = 0
                    else:
                        healths[robot] = 0
                        healths[combatant] = 0


        return [healths[robot] for robot in range(n) if healths[robot] > 0]        