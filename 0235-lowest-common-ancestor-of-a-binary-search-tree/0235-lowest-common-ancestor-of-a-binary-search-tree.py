# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def _find_way_to(self, node_to_find: 'TreeNode', current_root: 'TreeNode'):
        '''Return local way from current_root to node_to_find '''
        
        local_way = [current_root]
        
        if current_root.val == node_to_find.val:
            return local_way
        
        if current_root.left:
            sub_way = self._find_way_to(node_to_find, current_root.left)
            if sub_way:
                local_way.extend(sub_way)
                return local_way

        if current_root.right:
            sub_way = self._find_way_to(node_to_find, current_root.right)
            if sub_way:
                local_way.extend(sub_way)
                return local_way
                    
        return None
        
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        way_to_p = self._find_way_to(p, root)
        way_to_q = self._find_way_to(q, root)

        
        for ancestor_of_p in reversed(way_to_p):
            if ancestor_of_p.val in [node.val for node in way_to_q]:
                return ancestor_of_p
        