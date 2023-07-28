# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p == q:
            return p
        if not root:
            return None

        nodes_to_find = (p, q)

        def find_node(root: TreeNode, node: TreeNode, path: list[TreeNode]) -> list[TreeNode] | None:
                if not root:
                    return None

                path.append(root)
                if root == node:
                    return path

                if root.left:
                    left_path = find_node(root.left, node, path)
                    if left_path[-1] == node:
                        return left_path

                if root.right:
                    right_path = find_node(root.right, node, path)
                    if right_path[-1] == node:
                        return right_path

                path.pop()
                return path
        
        
        path = deque()
        first_node = p
        first_path = find_node(root, first_node, path).copy()
        
        path.clear()
        second_node = p if first_path[-1] == q else q
        second_path = find_node(root, second_node, path)
      

        while first_path:         
            node = first_path.pop()
            if node in second_path:
                return node

        return None