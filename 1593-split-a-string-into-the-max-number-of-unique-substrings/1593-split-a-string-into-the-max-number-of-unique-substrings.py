class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.string = s
        self.n = len(s)
        self.max_split_count = 0
        self.seen = set()
        self.backtrack(0,0)
        return self.max_split_count

    def backtrack(self, start, current_count):
        if start >= self.n:
            self.max_split_count = max(self.max_split_count, current_count)
        if current_count + (self.n  - start) <= self.max_split_count:
            return 
        for end in range(start+1, self.n+1):
            test_sub_string = self.string[start:end]
            if test_sub_string not in self.seen:
                self.seen.add(test_sub_string)
                new_start = end
                self.backtrack(new_start, current_count + 1)
                self.seen.remove(test_sub_string)
        return