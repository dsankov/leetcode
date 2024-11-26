class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        m = len(board)
        n = len(board[0])
        used_cells = [[False] * n for _ in range(m)]
    
        
        def backtrack(board, word, used_cells, row, col, word_ptr):
            if word_ptr == len(word):
                return True
            if board[row][col] != word[word_ptr]:
                return False
            if word_ptr == len(word) - 1:
                return True

            used_cells[row][col] = True
            for d_row, d_col in directions:
                if 0 <= row + d_row < m and 0 <= col + d_col < n and not used_cells[row + d_row][col + d_col]:
                    if backtrack(board, word, used_cells, row + d_row, col + d_col, word_ptr + 1):
                        return True
            used_cells[row][col] = False
            return False
        
        for start_row in range(m):
            for start_col in range(n):
                if backtrack(board, word, used_cells, start_row, start_col, word_ptr=0):
                    return True
        return False

        