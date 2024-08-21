class Solution:
    def strangePrinter(self, s: str) -> int:
        s = "".join(char for char, _ in itertools.groupby(s))

        memo = {}

        def _minimum_turns(start, end) -> int:
            if start > end:
                return 0
            if (start, end) in memo:
                return memo[(start,end)]
            min_turns = 1 + _minimum_turns(start+1, end)

            for split_point in range(start+1, end+1):
                if s[split_point] == s[start]:
                    turns_with_split = _minimum_turns(start, split_point - 1) + _minimum_turns(split_point + 1, end)
                    min_turns = min(min_turns, turns_with_split)

            memo[(start,end)] = min_turns
            return min_turns

        return _minimum_turns(0, len(s)-1)
