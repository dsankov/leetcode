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
        calculated_min_distance = [[0] * (num_factories + 1) for _ in range(num_robots + 1)]
        for robot in range(num_robots):
            calculated_min_distance[robot][num_factories] = math.inf

        for robot in range(num_robots - 1, -1, -1):
            for factory in range(num_factories - 1, -1, -1):
                use_factory = (
                    abs(robots[robot] - factories[factory])
                    + calculated_min_distance[robot + 1][factory + 1]
                )
                skip_factory = calculated_min_distance[robot][factory + 1]

                calculated_min_distance[robot][factory] = min(use_factory, skip_factory)

        return calculated_min_distance[0][0]
