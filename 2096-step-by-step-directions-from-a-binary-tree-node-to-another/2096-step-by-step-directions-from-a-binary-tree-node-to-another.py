# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find_path_to_node(root: TreeNode, value: int, path: list[str]) -> bool:
            if not root:
                return False

            if root.val == value:
                return True
                
            path.append("L")
            if find_path_to_node(root.left, value, path):
                return True
            path.pop()

            path.append("R")
            if find_path_to_node(root.right, value, path):
                return True
            path.pop()

            return False

        start_path = []
        dest_path = []
        find_path_to_node(root, startValue, start_path)
        find_path_to_node(root, destValue, dest_path)
        common_path_lenght = 0
        while (
            common_path_lenght < len(start_path)
            and common_path_lenght < len(dest_path)
            and start_path[common_path_lenght] == dest_path[common_path_lenght]
        ):
            common_path_lenght += 1

        result = []
        result.extend("U" * (len(start_path) - common_path_lenght))
        result.extend(dest_path[common_path_lenght:])

        return "".join(result) 
        