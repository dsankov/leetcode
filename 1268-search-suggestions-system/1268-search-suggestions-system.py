class Solution:
    class TrieNode:
        def __init__(self):
            self.value = None
            self.children = [None] * 26
            self.terminal = False

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = self.TrieNode()
        for product in products:
            curr_node = root
            for char in product:
                if not curr_node.children[ord(char) - ord("a")]:
                    curr_node.children[ord(char) - ord("a")] = self.TrieNode()
                curr_node = curr_node.children[ord(char) - ord("a")]
            curr_node.value = product
            curr_node.terminal = True

        result = []
        search_failed = False
        curr_node = root
        for char in searchWord:
            if search_failed:
                result.append([])
                continue
            if not curr_node.children[ord(char) - ord("a")]:
                result.append([])
                search_failed = True
                continue

            curr_node = curr_node.children[ord(char) - ord("a")]
            result.append(self.find_sugestions(curr_node))
        return result

    def find_sugestions(self, node):
        nodes_stack = [node]
        result = []
        while nodes_stack:
            curr_node = nodes_stack.pop()
            if curr_node.terminal:
                result.append(curr_node.value)
            
            for char in range(25, -1, -1):
                if curr_node.children[char]:
                    nodes_stack.append(curr_node.children[char])
            
            if len(result) == 3:
                return result
        return result
    

        