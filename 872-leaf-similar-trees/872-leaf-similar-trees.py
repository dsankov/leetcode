# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leafs(root) -> int:
            if not root:
                yield  None
            elif not root.left and not root.right:
                yield root.val
            else:
                if root.left:
                    yield from leafs(root.left)
                if root.right:
                    yield from leafs(root.right)
             
 
        for leaf1, leaf2 in itertools.zip_longest(leafs(root1), leafs(root2)):
            if leaf1 != leaf2:
                return False

        return True
