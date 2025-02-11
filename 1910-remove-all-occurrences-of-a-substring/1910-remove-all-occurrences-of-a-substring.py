class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        part_len = len(part)
        part_array = list(part)
        part_lps = [0] * (part_len + 1)
        stack = []
        part_idx = 0
        match_len = 0

        for s_idx, s_char in enumerate(s):
            stack.append(s_char)
            if len(stack) < part_len:
                continue
            if stack[-part_len:] == part_array:
                for _ in range(part_len):
                    stack.pop()

        return "".join(stack)
        #             


        #     part_char = part[part_idx]
        #     char_to_check = part[match_len]
        #     # print(f"\n{part_idx}->{part_char}")
        #     if part_char != s_char:
        #         part_idx = 0
        #         stack.append((s_char, part_idx))


        #         # if match_len == 0:
        #         #         pass
        #         # else:
        #         #         prev_char = match_len - 1
        #         #         if prev_char == s_char:    
        #         #             last_match_char, last_match_len = stack[-1]
        #         #             match_len = last_match_len
        #         #         else:
        #         #             match_len = 0
                    
        #         # print(f"! {s_idx}->{s_char} != {char_to_check}<-{match_len}")
        #         print(f"! \t Distinct char stack.append {s_char} {match_len}")

        #     else:
        #         # print(f"{s_idx}->{s_char} == {char_to_check}<-{match_len}")
        #         # print("11111111111111111")
        #         # match_len += 1
        #         if match_len == 0:
        #             part_idx = 0
        #         else:
        #             part_idx = part_lps[mach_len - 1]
        #         part_idx += 1





        #         stack.append((s_char, match_len))
        #         print(f"= \t Matched char stack.append {s_char} {match_len}")

        #         if match_len == part_len:
        #             # print("!!!!!!!!!")
        #             if not stack:
        #                 match_len = 0
        #             else:
        #                 last_match_char, last_match_len = stack[-1]
        #                 match_len = last_match_len
                   
        #             # print(f"{match_len=}")
        #             print(f"\t\t Removed from stack {stack}")

        #     print(f"Stack at end {stack}\n")
                                    
