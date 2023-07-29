# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None

        
        nodes_queue = deque()
        nodes_queue.append(root)
        
        result = []

        while nodes_queue:
            rightmost_node = nodes_queue[-1]
            result.append(rightmost_node.val)
            
            next_level = deque()
            while nodes_queue:
                node = nodes_queue.popleft()
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            nodes_queue = next_level

        return result


