# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter_with_depth(root):
            ''' retunrs tuple: (diameter, depth) '''
            if not root:
                return (0, 0)
            left_diameter,  left_depth  = diameter_with_depth(root.left)
            right_diameter, right_depth = diameter_with_depth(root.right)
            depth = max(left_depth, right_depth) + 1
            diameter = max(left_diameter, right_diameter, left_depth+right_depth)
            return (diameter, depth)

        diameter, depth = diameter_with_depth(root)
        return diameter

        

        