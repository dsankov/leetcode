# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        max_id = 10 ** 5
        nodes = [None] * (max_id + 1)
        children = set()
        parents = set()
        for parent, child, is_left in descriptions:
            parents.add(parent)
            children.add(child)
            if not nodes[parent]:
                nodes[parent] = TreeNode(parent)
            if not nodes[child]:
                nodes[child] = TreeNode(child)
            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
        root = parents - children
        root = next(iter(root))
        return nodes[root]
        