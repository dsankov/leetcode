# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
       
        def del_node(root, key):
            if not root:
                return None
            if root.val == key:
                if not root.right:
                    return root.left
                
                minimal_right_node_parent = root.right
                if not minimal_right_node_parent.left:
                    minimal_right_node_parent.left = root.left
                    return minimal_right_node_parent
                # else
                minimal_right_node =  minimal_right_node_parent.left
                
                while minimal_right_node.left:
                    minimal_right_node_parent = minimal_right_node
                    minimal_right_node = minimal_right_node.left
                
                minimal_right_node_parent.left = minimal_right_node.right 
                minimal_right_node.left = root.left
                minimal_right_node.right = root.right
                
                return minimal_right_node

            if key > root.val:
                root.right = del_node(root.right, key)
            elif key < root.val:
                root.left = del_node(root.left, key)
            return root
            

        return del_node(root, key)