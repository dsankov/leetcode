# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
#         def get_traversal_items(traversal: str):
#             idx = 0
#             while idx < len(traversal):
#                 level = 0
#                 while traversal[idx] == "-":
#                     level += 1
#                     idx += 1
#                 value = 0
#                 while idx < len(traversal) and traversal[idx].isdigit():
#                     value = value * 10 + int(traversal[idx])
#                     idx += 1
#                 yield (level, value)

#         traversal_items = get_traversal_items(traversal)
#         root_level, root_value = next(traversal_items)
#         root_node = TreeNode(root_value)
#         node_stack = [(root_level, root_node)]

#         while traversal_items:
#             next_node_level, next_node_value = next(traversal_items)

#             while node_stack:
#                 print (node_stack)
#                 cur_level, cur_node = node_stack[-1]
#                 print(f"{cur_level=} {cur_node.val=}")

#                 print(f"{next_node_level=} {next_node_value=}")

#                 if next_node_level == cur_level + 1:
#                     cur_node.left = TreeNode(next_node_value)
#                     node_stack.append((next_node_level, cur_node.left))
#                     print(node_stack)
#                     next_node_level, next_node_value = next(traversal_items)
                
#                     if next_node_level == cur_level + 1:
#                         cur_node.right = TreeNode(next_node_value)
#                         node_stack.append((next_node_level, cur_node.right))
#                         print(node_stack)
#                         next_node_level, next_node_value = next(traversal_items)
#                     # else:
#                     #     node_stack.pop()
#                 elif node_stack:
                    
#                     node_stack.pop()

#         return root_node   

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        levels = []  # List to track the last node at each depth
        index, n = 0, len(traversal)

        while index < n:
            # Count depth (number of dashes)
            depth = 0
            while index < n and traversal[index] == "-":
                depth += 1
                index += 1

            # Extract node value
            value = 0
            while index < n and traversal[index].isdigit():
                value = value * 10 + int(traversal[index])
                index += 1

            # Create the new node
            node = TreeNode(value)

            # Adjust levels list to match the current depth
            if depth < len(levels):
                levels[depth] = node
            else:
                levels.append(node)

            # Attach the node to its parent
            if depth > 0:
                parent = levels[depth - 1]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node

        # The root node is always at index 0
        return levels[0]