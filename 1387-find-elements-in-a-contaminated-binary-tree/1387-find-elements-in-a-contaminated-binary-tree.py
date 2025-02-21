# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.present_nodes = set()
        nodes_queue = [(root, 0)]
        while nodes_queue:
            cur_node, cur_val = nodes_queue.pop()
            self.present_nodes.add(cur_val)
            if left_child := cur_node.left:
                left_val = cur_val * 2 + 1
                nodes_queue.append((left_child, left_val))
            if right_child := cur_node.right:
                right_val = cur_val * 2 + 2
                nodes_queue.append((right_child, right_val))
        

    def find(self, target: int) -> bool:
        return target in self.present_nodes
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)