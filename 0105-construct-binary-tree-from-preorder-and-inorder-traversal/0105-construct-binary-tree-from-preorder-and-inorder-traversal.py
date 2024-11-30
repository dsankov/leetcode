# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from pprint import pp, pprint
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index_of = {value: index for index, value in enumerate(inorder)}
        
        def build_node(pre_start, in_start, tree_size):
            if tree_size == 0:
                return None

            pre_root_index = pre_start
            root_value = preorder[pre_root_index]
            in_root_index = inorder_index_of[root_value]

            left_subtree_size = in_root_index - in_start
            right_subtree_size = tree_size - 1 - left_subtree_size
            root_node = TreeNode(root_value)
            
            root_node.left = build_node(pre_start=pre_root_index + 1, 
                                        in_start=in_root_index - left_subtree_size, 
                                        tree_size=left_subtree_size)
            root_node.right = build_node(pre_start=pre_root_index + 1 + left_subtree_size, 
                                         in_start=in_root_index + 1, 
                                         tree_size=right_subtree_size)
            return root_node
            
        root = build_node(pre_start=0, in_start=0, tree_size=len(preorder))
        return root
        