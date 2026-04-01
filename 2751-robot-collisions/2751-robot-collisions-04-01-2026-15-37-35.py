from collections import namedtuple

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        sorted_robots = sorted([(positions[idx], idx) for idx in range(n)])
        going_left = []
        going_right_stack = []
        for idx, ( _ , robot) in enumerate(sorted_robots):
            if directions[robot] == "R":
                going_right_stack.append(robot)
                continue

            while going_right_stack:
                enemy = going_right_stack.pop()
                if healths[enemy] > healths[robot]:
                    healths[enemy] -= 1
                    going_right_stack.append(enemy)
                    break
                elif healths[enemy] < healths[robot]:
                    healths[robot] -= 1
                else:
                    break 
            else:
                going_left.append(robot)        

        going_left = set(going_left)
        going_right_stack = set(going_right_stack) 
        result = []
        for robot in range(n):
            if robot in going_left or robot in going_right_stack:
                result.append(healths[robot])


        return result
        