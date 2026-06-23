class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        word_len = len(beginWord)
        num_words = len(wordList)

        word_queue = deque([beginWord])
        begin_set = {beginWord}
        end_set = {endWord}
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
                # cur_word_as_list = list(cur_word)

                for letter_pos in range(word_len):
                    # original_letter = cur_word_as_list[letter_pos]
                    for new_letter in string.ascii_lowercase:
                        if cur_word[letter_pos] == new_letter:
                            continue
                        # cur_word_as_list[letter_pos] = new_letter
                        # new_word = "".join (cur_word_as_list)
                        new_word = cur_word[:letter_pos] + new_letter + cur_word[letter_pos + 1:]
                        if new_word not in word_set:
                            continue
                        if new_word in seen_words:
                            continue
                        word_queue.append(new_word)
                        seen_words.add(new_word)
                    # cur_word_as_list[letter_pos] = original_letter


                # for next_word in graph[cur_word]:
                #     if next_word in seen_words:
                #         continue
                #     seen_words.add(cur_word)
                #     word_queue.append(next_word)

        return 0