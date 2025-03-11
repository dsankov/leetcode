class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_seen_position = {"a": -1, "b": -1, "c": -1}
        total_substrings_count = 0
        for position, letter in enumerate(s):
            last_seen_position[letter] = position
            total_substrings_count += 1 + min(last_seen_position.values()) 
        return total_substrings_count