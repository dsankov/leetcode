# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        assert root is not None

        nodes_queue = deque([(root, [])])
        while nodes_queue:
            level_width = len(nodes_queue)
            # print(level_width)
            level_leaves = []
            leaf_paths = []
            for _ in range(level_width):
                node, path = nodes_queue.popleft()
                path.append(node)
                if not node.left and not node.right:
                    level_leaves.append(node)
                    leaf_paths.append(path)
                else:
                    if node.left:
                        nodes_queue.append((node.left, path.copy()))
                    if node.right:
                        nodes_queue.append((node.right, path.copy()))
        # print (level_leaves)
        # print(leaf_paths)
        some_path = leaf_paths[0]
        for step in range(len(some_path) - 1, -1, -1):
            if all(some_path[step] == path[step] for path in leaf_paths):
                return some_path[step]
        # print(some_path)

        return root