class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if n * m != len(original):
            return []
        return [original[i: i+n] for i in range(0, n * m, n)]
        