DIRS = [[1, 0], [0, 1], [-1, 0], [0, -1]]
class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.perimetr = (width + height - 2) * 2
        self.x = 0
        self.y = 0
        self.dir = 0

    def getPos(self) -> List[int]:
        return [self.x, self.y]
        

    def getDir(self) -> str:
        return ["East", "North", "West", "South"][self.dir]


    def _dist_to_border(self) -> int:
        match self.dir:
            case 0:
                return self.width - 1 - self.x
            case 1:
                return self.height - 1 - self.y
            case 2:
                return self.x
            case 3:
                return self.y

    def step(self, num: int) -> None:
        # step = 0
        # while step < num:
        #     next_x = self.x + DIRS[self.dir][0]
        #     next_y = self.y + DIRS[self.dir][1]
        #     if 0 <= next_x < self.width and 0 <= next_y < self.height:
        #         step += 1
        #         self.x = next_x
        #         self.y = next_y
        #         continue
            
        #     self.dir = (self.dir + 1) % 4

        remain_steps = num
        dist_to_border = self._dist_to_border()
        if remain_steps <= dist_to_border:
            self.x += remain_steps * DIRS[self.dir][0]
            self.y += remain_steps * DIRS[self.dir][1]
            return

        self.x += dist_to_border * DIRS[self.dir][0]
        self.y += dist_to_border * DIRS[self.dir][1]
        remain_steps -= dist_to_border
        if remain_steps > 0:
            self.dir = (self.dir + 1) % 4
        remain_steps %= self.perimetr
        while remain_steps > 0:
            dist_to_border = self._dist_to_border()
            if remain_steps <= dist_to_border:
                self.x += remain_steps * DIRS[self.dir][0]
                self.y += remain_steps * DIRS[self.dir][1]
                return

            self.x += dist_to_border * DIRS[self.dir][0]
            self.y += dist_to_border * DIRS[self.dir][1]
            remain_steps -= dist_to_border
            if remain_steps > 0:
                self.dir = (self.dir + 1) % 4