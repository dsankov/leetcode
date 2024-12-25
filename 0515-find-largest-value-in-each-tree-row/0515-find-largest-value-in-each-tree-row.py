# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        nodes_queue = deque()
        nodes_queue.append(root)
        max_per_level = []
        while nodes_queue:
            curr_max = -inf
            for _ in range(len(nodes_queue)):
                curr_node = nodes_queue.popleft()
                curr_max = max(curr_max, curr_node.val)
                if curr_node.left:
                    nodes_queue.append(curr_node.left)
                if curr_node.right:
                    nodes_queue.append(curr_node.right)
            max_per_level.append(curr_max)
        return max_per_level

        