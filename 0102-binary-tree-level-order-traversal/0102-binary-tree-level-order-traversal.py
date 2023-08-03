# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        tree_level = 0
        nodes_queue = deque()
        nodes_queue.append([tree_level, root])
        level_slice = []
        last_seen_level = 0
        while nodes_queue:
            current_level, current_node = nodes_queue.popleft()
            if not current_node:
                continue
            # print (f"eximing level:{current_level} val={current_node.val}")
            if current_level == last_seen_level:
                level_slice.append(current_node.val)
                # print (f"appending to level:{current_level} node with val={current_node.val}")

            else:
                result.append(level_slice)
                level_slice = []
                level_slice.append(current_node.val)
                last_seen_level = current_level

            nodes_queue.append([current_level+1, current_node.left])
            nodes_queue.append([current_level+1, current_node.right])

        result.append(level_slice)
        return result



