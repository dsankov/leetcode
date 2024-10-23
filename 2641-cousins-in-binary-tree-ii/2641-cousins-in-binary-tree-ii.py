# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        levels_sums = []
        nodes_queue = deque([root])
        while nodes_queue:
            level_size = len(nodes_queue)
            level_sum = 0
            for _ in range(level_size):
                curr_node = nodes_queue.popleft()
                level_sum += curr_node.val
                for child in (curr_node.left, curr_node.right):
                    if child:
                        nodes_queue.append(child)
            levels_sums.append(level_sum)

        root.val = 0
        nodes_queue = deque([root])
        level_index = 1
        while nodes_queue:
            level_size = len(nodes_queue)
            for _ in range(level_size):
                curr_node = nodes_queue.popleft()
                childrens_sum = (
                    curr_node.left.val if curr_node.left else 0
                ) + (
                    curr_node.right.val if curr_node.right else 0
                )
                for child in (curr_node.left, curr_node.right):
                    if child:
                        child.val = levels_sums[level_index] - childrens_sum
                        nodes_queue.append(child)
            level_index += 1
        return root