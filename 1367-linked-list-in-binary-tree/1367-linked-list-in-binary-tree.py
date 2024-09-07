# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # if not root:
        #     return False
        nodes_stack = [root]

        while nodes_stack:
            node = nodes_stack.pop()

            if self.is_match(node, head):
                return True
            if node.left:
                nodes_stack.append(node.left)
            if node.right:
                nodes_stack.append(node.right)

        return False

    def is_match(self, tree_node, list_node) -> bool:
        compare_stack = [(tree_node, list_node)]
        while compare_stack:
            current_tree_node, current_list_node = compare_stack.pop()
            while current_tree_node and current_list_node:
                if current_tree_node.val != current_list_node.val:
                    break
                current_list_node = current_list_node.next

                if current_list_node:
                    if current_tree_node.left:
                        compare_stack.append((current_tree_node.left, current_list_node))
                    if current_tree_node.right:
                        compare_stack.append((current_tree_node.right, current_list_node))
                    break
            if not current_list_node:
                return True

        return False