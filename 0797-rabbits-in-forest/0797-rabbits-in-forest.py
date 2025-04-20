class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers = Counter(answers)
        result = 0
        for answer_value, answer_count in answers.items():
            group_size = answer_value + 1
            group_num = math.ceil(answer_count / group_size)
            result += group_size * group_num
        return result