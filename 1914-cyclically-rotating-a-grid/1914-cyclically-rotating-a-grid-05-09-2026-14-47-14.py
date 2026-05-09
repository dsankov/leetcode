class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def layer_iter(m, n):
            for col in range(n - 1):
                yield (0,  col)
            for row in range(m - 1):
                yield (row, n-1)
            for n_col in range(n-1):
                yield (m - 1, n - 1 - n_col)
            for n_row in range(m - 1):
                yield (m - 1 - n_row, 0)
             



        m, n = len(grid), len(grid[0])
        result = [[0] * n  for _ in range(m)]

        num_layers = min(m, n) // 2
        for layer_no in range(num_layers):
            layer_m = m - 2 * layer_no
            layer_n = n - 2 * layer_no
            layer_len = (layer_m + layer_n - 2) * 2
            layer_k = k % layer_len

            original_layer = layer_iter(layer_m, layer_n)
            shifted_layer = itertools.cycle(layer_iter(layer_m, layer_n))
            for _ in range(layer_k):
                next(shifted_layer)
            
            r0 = c0 = layer_no
            for d_r, d_c in original_layer:
                sh_r, sh_c = next(shifted_layer)
                result[r0 + d_r][c0 + d_c] = grid[r0 + sh_r][c0 + sh_c]

        return result            
