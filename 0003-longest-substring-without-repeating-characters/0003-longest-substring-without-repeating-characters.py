class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        longest_substr_seen_before = ''
        max_lenght = 0
        current_lenght = 0
        for char_id in range(len(s)):
            if s[char_id] in longest_substr_seen_before:
                char_previous_entry = longest_substr_seen_before.index(s[char_id])
                longest_substr_seen_before = longest_substr_seen_before[char_previous_entry + 1:]    
            
            longest_substr_seen_before = longest_substr_seen_before + s[char_id]
            current_lenght = len(longest_substr_seen_before)
            max_lenght = max(max_lenght, current_lenght)

        return max_lenght