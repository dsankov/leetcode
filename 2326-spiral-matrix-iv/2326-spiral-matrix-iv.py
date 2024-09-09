# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        direction = itertools.cycle(DIRECTIONS)
        result = [[-1] * n for _ in range(m)]
        row, col = 0, 0
        d_row, d_col = next(direction)
        while head:
            result[row][col] = head.val
            next_row = row + d_row
            next_col = col + d_col
            if not (
                0 <= next_row < m
                and 0 <= next_col < n
                and result[next_row][next_col] == -1
            ):
                d_row, d_col = next(direction)
            row += d_row
            col += d_col
            head = head.next
        return result

        