from collections import namedtuple


class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        Robot = namedtuple("Robot", "pos distance")
        robots = [Robot(robot, distance) for robot, distance in zip(robots, distance)]
        robots.sort()
        walls.sort()

        rightmost_dummy_robot = Robot(10**9 + 1, 0)
        robots.append(rightmost_dummy_robot)
        print(robots)

        def count_walls(left, right):
            if left > right:
                return 0
            return bisect.bisect_right(walls, right) - bisect.bisect_left(walls, left)

        if n == 1:
            return max(
                count_walls(robots[0].pos - robots[0].distance, robots[0].pos),
                count_walls(robots[0].pos, robots[0].pos + robots[0].distance),
            )

        dp = [{"left": 0, "right": 0} for _ in range(n)]
        dp[0]["left"] = count_walls(robots[0].pos - robots[0].distance, robots[0].pos)
        dp[0]["right"] = count_walls(
            robots[0].pos, min(robots[0].pos + robots[0].distance, robots[1].pos - 1)
        )
        for robot in range(1, n):
            right_range = min(
                robots[robot].pos + robots[robot].distance,
                robots[robot + 1].pos - 1,
            )
            dp[robot]["right"] = max(
                dp[robot - 1]["left"], dp[robot - 1]["right"]
            ) + count_walls(
                robots[robot].pos,
                right_range,
            )

            left_range = max(
                robots[robot].pos - robots[robot].distance, robots[robot - 1].pos + 1
            )
            case_prev_shoot_left = dp[robot - 1]["left"] + count_walls(
                left_range, robots[robot].pos
            )

            prev_right_range = min(
                robots[robot - 1].pos + robots[robot - 1].distance,
                robots[robot].pos - 1,
            )

            case_prev_shoot_right = (
                dp[robot - 1]["right"]
                + count_walls(left_range, robots[robot].pos)
                - count_walls(left_range, prev_right_range)
            )
            dp[robot]["left"] = max(case_prev_shoot_left, case_prev_shoot_right)
        return max(dp[n - 1]["left"], dp[n - 1]["right"])
