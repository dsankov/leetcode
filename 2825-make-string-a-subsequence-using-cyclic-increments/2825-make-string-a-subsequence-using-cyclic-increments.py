class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        next_char = {chr(char): chr(char + 1) for char in range(ord("a"), ord("z"))}
        next_char["z"] = "a"
        
        str_ptr = 0
        for pattern_char in str2:
            while str_ptr < len(str1):
                str_ptr += 1
                if pattern_char in (str1[str_ptr-1], next_char[str1[str_ptr-1]]):
                    break
            else:
                return False 

        return True