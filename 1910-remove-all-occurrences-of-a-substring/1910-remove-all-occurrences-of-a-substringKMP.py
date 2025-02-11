class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        part_len = len(part)
        s_len = len(s)

        part_lps = [0] * part_len

        curr_pattern_idx = 1
        prefix_len = 0

        while curr_pattern_idx < part_len:
            if part[curr_pattern_idx] == part[prefix_len]:
                part_lps[curr_pattern_idx] = prefix_len + 1
                prefix_len += 1
                curr_pattern_idx += 1
            elif prefix_len == 0:
                part_lps[curr_pattern_idx] = 0
                curr_pattern_idx += 1
            else:
                prefix_len = part_lps[prefix_len - 1]

        char_stack = []
        pattern_indices = [0] * (s_len + 1)
        s_idx = 0
        pattern_idx = 0
        while s_idx < s_len:
            cur_char = s[s_idx]
            char_stack.append(cur_char)

            if cur_char == part[pattern_idx]:
                pattern_indices[len(char_stack)] = pattern_idx + 1
                pattern_idx += 1

                if pattern_idx == part_len:
                    for _ in range(part_len):
                        char_stack.pop()


                if not char_stack:
                    pattern_idx = 0
                else:
                    pattern_idx = pattern_indices[len(char_stack)]        
            
            else:        
                if pattern_idx != 0:
                    pattern_idx = part_lps[pattern_idx - 1]
                    s_idx -= 1
                    char_stack.pop()
                else:
                    pattern_indices[len(char_stack)] = 0

            s_idx += 1

        return "".join(char_stack)
       