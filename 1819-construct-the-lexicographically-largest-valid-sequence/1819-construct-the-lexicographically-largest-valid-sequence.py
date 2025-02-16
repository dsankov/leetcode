class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        self.n = n
        self.is_num_used = [False] * (n + 1)
        self.sequence = [0] * (2 * n - 1)
        self.generate_sequence(0)
        return self.sequence

    def generate_sequence(self, cur_index):
        if cur_index == 2 * self.n - 1:
            return True
        if self.sequence[cur_index] != 0:
            return self.generate_sequence(cur_index + 1)
        
        for cur_num in range(self.n, 0, -1):
            if self.is_num_used[cur_num]:
                continue

            self.is_num_used[cur_num] = True
            self.sequence[cur_index] = cur_num

            if cur_num == 1:
                if self.generate_sequence(cur_index + 1):
                    return True

            elif (cur_index + cur_num < 2 * self.n - 1
                and self.sequence[cur_index + cur_num] == 0
            ):
                self.sequence[cur_index + cur_num] = cur_num
                if self.generate_sequence(cur_index + 1):
                    return True
                self.sequence[cur_index + cur_num] = 0

            self.is_num_used[cur_num] = False
            self.sequence[cur_index] = 0

        return False
