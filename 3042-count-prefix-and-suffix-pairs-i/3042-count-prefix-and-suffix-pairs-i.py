from pprint import pp
class Trie:
    class TrieNode:
        def __init__(self, word_id):
            self.children = {}
            self.seen_in = set((word_id,))
    
    def __init__(self):
        self.root = self.TrieNode(-1)

    def add_word(self, word_id: int, word: str) -> set:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = self.TrieNode(word_id)
            node = node.children[char]
            node.seen_in.add(word_id)
    
    def prefix_of(self, prefix: str) -> set:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return set()
            node = node.children[char]
        return node.seen_in

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        prefix_trie = Trie()
        suffix_trie = Trie()
        result = 0
        for word_id, word in enumerate(words[::-1]):
            reversed_word = word[::-1]
            result += len(
                        prefix_trie.prefix_of(word)
                        & suffix_trie.prefix_of(reversed_word)
                        )
            prefix_trie.add_word(word_id, word)
            suffix_trie.add_word(word_id, reversed_word)
        return result