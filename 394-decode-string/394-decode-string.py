class Solution:
    def decodeString(self, s: str) -> str:
        strings = deque()
        nums = deque()
        current_str = ""
        current_num = 0
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 +int(char)
            elif char == "[":             
                nums.append(current_num)
                strings.append(current_str)
                current_str = ""
                current_num = 0
            elif char == "]":
                previous_str = strings.pop()
                previous_num = nums.pop()
                current_str = previous_str + current_str * previous_num
            else:
                current_str += char 

        return current_str
        