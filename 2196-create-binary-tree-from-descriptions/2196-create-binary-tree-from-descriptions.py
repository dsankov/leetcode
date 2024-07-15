# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        all_nodes = set()
        child_nodes = set()
        graph = {}
        for parent, child, is_left in descriptions:
            all_nodes.add(parent)
            all_nodes.add(child)
            child_nodes.add(child)
            if parent not in graph:
                graph[parent] = TreeNode(val=parent)
            if child not in graph:
                graph[child] = TreeNode(val=child)
            if is_left:
                graph[parent].left = graph[child]
            else:
                graph[parent].right = graph[child]

        return graph[(all_nodes - child_nodes).pop()]

            