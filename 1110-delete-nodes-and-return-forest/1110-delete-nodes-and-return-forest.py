# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        forest = []
        nodes_queue = deque()
        nodes_queue.append(root)

        while nodes_queue:
            cur_node = nodes_queue.popleft()
            # nodes_queue.extend([cur_node.left, cur_node.right])
            if cur_node.left:
                nodes_queue.append(cur_node.left)
                if cur_node.left.val in to_delete:
                    cur_node.left = None
            if cur_node.right:
                nodes_queue.append(cur_node.right)
                if cur_node.right.val in to_delete:
                    cur_node.right = None
            if cur_node.val in to_delete:
                if cur_node.left:
                    forest.append(cur_node.left)
                if cur_node.right:
                    forest.append(cur_node.right)
        if root.val not in to_delete:
            forest.append(root)

        return forest        