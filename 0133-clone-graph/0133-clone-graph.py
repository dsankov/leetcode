"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        already_copied_nodes = {}
        def dfc(node) -> Node:
            if not node:
                return None
            
            if node.val in already_copied_nodes:
                return already_copied_nodes[node.val]
            
            copied_node = Node(node.val)
            already_copied_nodes[node.val] = copied_node
            for neighbor in node.neighbors:
                copied_node.neighbors.append(dfc(neighbor))
                
            return copied_node
        
        
        return dfc(node)