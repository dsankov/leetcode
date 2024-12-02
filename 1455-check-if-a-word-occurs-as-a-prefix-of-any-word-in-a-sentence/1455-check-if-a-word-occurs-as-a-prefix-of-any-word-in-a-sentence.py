from pprint import pp
class TrieNode():
    def __init__(self, word_num: int, value: str=None):
        self.value = value
        self.children = dict()
        self.word_num = word_num

class Trie():
    def __init__(self):
        self.root = TrieNode(0)
        self.word_num = 1

    def add_word(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(self.word_num, char)
            node = node.children[char]
        self.word_num += 1

    def search_prefix(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                return -1
            node = node.children[char]
            word_num = node.word_num
        return word_num



class Solution:

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence_trie = Trie()
        for word in sentence.split():
            sentence_trie.add_word(word)

        return sentence_trie.search_prefix(searchWord)

        