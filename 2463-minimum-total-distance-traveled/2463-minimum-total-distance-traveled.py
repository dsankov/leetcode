class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        self.robots = sorted(robot)
        self.factories = []
        sorted_factories = sorted(factory)
        for factory_position, factory_limit in sorted_factories:
            for i in range(factory_limit):
                self.factories.append(factory_position)

        self.num_robots = len(self.robots)
        self.num_factories = len(self.factories)
        self.calculated_min_distance = defaultdict(lambda: -1)
        return self.calculate_min_distance(start_robot=0, start_factory=0)

    def calculate_min_distance(self, start_robot, start_factory):
        if start_robot == self.num_robots:
            return 0
        if start_factory == self.num_factories:
            return math.inf
        if self.calculated_min_distance[(start_robot, start_factory)] != -1:
            return self.calculated_min_distance[(start_robot, start_factory)]

        use_factory = (
            abs(self.robots[start_robot] - self.factories[start_factory])
            + self.calculate_min_distance(start_robot + 1, start_factory + 1)
        )

        skip_factory = self.calculate_min_distance(start_robot, start_factory + 1)
        
        self.calculated_min_distance[(start_robot, start_factory)] = min(use_factory, skip_factory)
        return self.calculated_min_distance[(start_robot, start_factory)]