class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        VOWELS = {"a", "e", "i", "o", "u"}
        n = len(word)

        def contain_k_or_more_consonant(k: int) -> int:
            valid_substr_count = 0
            start_idx = end_idx = 0
            consonant_count = 0
            vowel_counts = defaultdict(int)
            
            while end_idx < n:
                curr_letter = word[end_idx]
                if curr_letter in VOWELS:
                    vowel_counts[curr_letter] += 1
                else:
                    consonant_count += 1

                while len(vowel_counts) == len(VOWELS) and consonant_count >= k:
                    valid_substr_count += (n - end_idx)
                    start_letter = word[start_idx]
                    if start_letter in VOWELS:
                        vowel_counts[start_letter] -= 1
                        if vowel_counts[start_letter] == 0:
                            del vowel_counts[start_letter]
                    else:
                        consonant_count -= 1
                    start_idx += 1 

                end_idx += 1

            return valid_substr_count

        return contain_k_or_more_consonant(k) - contain_k_or_more_consonant(k + 1)