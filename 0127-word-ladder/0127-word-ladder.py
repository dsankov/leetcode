class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        word_len = len(beginWord)
        
        word_queue = deque([beginWord])
        seen_words = set()
        steps = 0
        while word_queue:
            steps += 1
            level_width = len(word_queue)
            for _ in range(level_width):
                cur_word = word_queue.popleft()
                if cur_word == endWord:
                    return steps
                seen_words.add(cur_word)

                for letter_pos in range(word_len):
                    for new_letter in string.ascii_lowercase:
                        if cur_word[letter_pos] == new_letter:
                            continue

                        new_word = cur_word[:letter_pos] + new_letter + cur_word[letter_pos + 1:]
                        if new_word not in word_set or new_word in seen_words:
                            continue
                        
                        seen_words.add(new_word)
                        word_queue.append(new_word)
                   

        return 0