class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robots = sorted(robot)
        factories = []
        sorted_factories = sorted(factory)
        for factory_position, factory_limit in sorted_factories:
            for i in range(factory_limit):
                factories.append(factory_position)

        num_robots = len(robots)
        num_factories = len(factories)
        next_robot = [0] * (num_factories + 1)
        curr_robot = [0] * (num_factories + 1)

        for robot in range(num_robots - 1, -1, -1):
            # next_robot[num_factories] = math.inf
            curr_robot[num_factories] = math.inf
            for factory in range(num_factories - 1, -1, -1):
                use_factory = (
                    abs(robots[robot] - factories[factory])
                    + next_robot[factory + 1]
                )
                skip_factory = curr_robot[factory + 1]

                curr_robot[factory] = min(use_factory, skip_factory)
            next_robot = curr_robot[:]

        return curr_robot[0]
