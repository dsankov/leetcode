class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        n = len(moves)
        moves_count = Counter(moves)
        r, l = moves_count["R"], moves_count["L"]
        if r < l:
            r, l = l, r
        return n - l - l