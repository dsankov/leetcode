# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        LEFT = True
        RIGHT = False
        self.max_deep = 0

        def explore(root: TreeNode | None, came_from: bool, deep: int) -> None:
            # changes self.max_deep as result

            self.max_deep = max(self.max_deep, deep)
            if not root:
                return
            
            if came_from:   #LEFT
                explore(root.right, came_from=RIGHT, deep=deep+1)
                explore(root.left, came_from=LEFT, deep=0)
            else:           #RIGHT
                explore(root.left, came_from=LEFT, deep=deep+1)
                explore(root.right, came_from=RIGHT, deep=0)

        explore(root, came_from=LEFT,  deep=-1)
        explore(root, came_from=RIGHT, deep=-1)
        return self.max_deep
                
       
        
            

        