class Solution:
    def makeFancyString(self, s: str) -> str:
        s = list(s)
        read_ptr, write_ptr = 1, 1
        last_char_count = 1
        while read_ptr < len(s):
            if s[read_ptr] == s[write_ptr - 1]:
                last_char_count += 1
            else:
                last_char_count = 1
            if last_char_count < 3:
                s[write_ptr] = s[read_ptr]
                write_ptr += 1
            read_ptr += 1
        return "".join(s[:write_ptr])
        