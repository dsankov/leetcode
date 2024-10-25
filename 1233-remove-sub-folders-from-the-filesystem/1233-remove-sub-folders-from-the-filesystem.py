class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_leaf = False

class Solution:
    def removeSubfolders(self, paths: List[str]) -> List[str]:
        root = TrieNode()
        for path in paths:  # Build Trie
            current_path = root
            folders = path.split("/")
            for folder in folders[1:]: # Skip first empty (=="") part of path
                current_path = current_path.children[folder]
            current_path.is_leaf = True

        folders_queue = deque()
        folders_queue.append(("",root))
        result = []
        while folders_queue:
            current_path, current_folder = folders_queue.popleft()
            if current_folder.is_leaf:
                result.append(current_path)
            else:
                for child_path, child_node in current_folder.children.items():
                    folders_queue.append((current_path + "/" + child_path, child_node))
        return result