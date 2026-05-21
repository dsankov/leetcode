class TrieNode:
    def __init__(self):
        self.children = [None] * 10 
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1
        root = TrieNode()
        for num in arr1:
            cur_node = root
            for digit in map(int, str(num)):
                if not cur_node.children[digit]:
                    cur_node.children[digit] = TrieNode()
                cur_node = cur_node.children[digit]
        max_prefix_len = 0
        for num in arr2:
            cur_node = root
            cur_prefix_len = 0
            for digit in map(int, str(num)):
                if not cur_node.children[digit]:
                    break
                cur_prefix_len += 1
                cur_node = cur_node.children[digit]
            max_prefix_len = max(max_prefix_len, cur_prefix_len)

        return max_prefix_len
        