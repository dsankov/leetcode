class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        for row in range(m):
            shift = k * (1 if row % 2 == 0 else -1)
            for col in range(n):
                if mat[row][col] != mat[row][(col + n + shift) % n]:
                    return False
        return True