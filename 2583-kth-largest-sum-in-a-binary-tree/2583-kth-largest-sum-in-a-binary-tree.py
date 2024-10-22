# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        nodes_queue = deque([root])
        levels_sum = []
        while nodes_queue:
            level_size = len(nodes_queue)
            level_sum = 0
            for _ in range(level_size):
                curr_node = nodes_queue.popleft()
                level_sum += curr_node.val
                for child in (curr_node.left, curr_node.right):
                    if child:
                        nodes_queue.append(child)
            heappush(levels_sum, level_sum)
            if len(levels_sum) > k:
                heappop(levels_sum)

        return levels_sum[0] if len(levels_sum) == k else -1
        