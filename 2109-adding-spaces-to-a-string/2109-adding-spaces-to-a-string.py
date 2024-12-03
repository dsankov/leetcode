class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        space_index = 0
        result = []
        for char_index, char in enumerate(s):
            if space_index < len(spaces) and char_index == spaces[space_index]:
                result.append(" ")
                space_index += 1
            result.append(char)
        return "".join(result)
        