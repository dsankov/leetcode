class TrieNode:
    def __init__(self, origin_id=inf, origin_len=inf):
        self.children = [None] * 26
        self.origin_id = origin_id
        self.origin_len = origin_len

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, origin_id: int, word: str):
        word_len = len(word)
        cur_node = self.root
        for char in reversed(word):
            if word_len < cur_node.origin_len:
                cur_node.origin_len = word_len
                cur_node.origin_id = origin_id
            elif cur_node.origin_len == word_len and origin_id < cur_node.origin_id:
                cur_node.origin_id = origin_id

            child_ptr = ord(char) - ord("a")
            if not cur_node.children[child_ptr]:
                cur_node.children[child_ptr] = TrieNode(origin_id, word_len)

            cur_node = cur_node.children[child_ptr]

        if word_len < cur_node.origin_len:
            cur_node.origin_len = word_len
            cur_node.origin_id = origin_id
        elif cur_node.origin_len == word_len and origin_id < cur_node.origin_id:
            cur_node.origin_id = origin_id

    def find_LCS_id(self, word):
        cur_node = self.root
        for char in reversed(word):
            char_ptr = ord(char) - ord("a")
            if not cur_node.children[char_ptr]:
                return cur_node.origin_id
            cur_node = cur_node.children[char_ptr]
        return cur_node.origin_id

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        words_trie = Trie()
        for word_id, word in enumerate(wordsContainer):
            words_trie.add_word(word_id, word)
        ans = []
        for query in wordsQuery:
            LCS_id = words_trie.find_LCS_id(query)
            ans.append(LCS_id)
        return ans
        