class Solution:
    def numTilings(self, n: int) -> int:
        filled_column_states    = [0, 0, 1, 2]
        gaped_column_states     = [0, 0, 1, 1]
        
        for i in range(4, n + 2):
            filled_column_state = filled_column_states[i - 1] + filled_column_states[i - 2] +  2 * gaped_column_states[i - 1]
            gaped_column_state = gaped_column_states[i - 1] + filled_column_states[i - 2]
            filled_column_states.append(filled_column_state)
            gaped_column_states.append(gaped_column_state)

        return filled_column_states[n + 1] % (10**9 + 7)
