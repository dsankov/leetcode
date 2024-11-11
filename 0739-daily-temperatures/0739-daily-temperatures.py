class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        warmer_days_stack = []
        answer = [0] * len(temperatures)
        for day, temperature in enumerate(temperatures):
            while warmer_days_stack and temperatures[warmer_days_stack[-1]] < temperature:
                passed_colder_day = warmer_days_stack.pop()
                answer[passed_colder_day] = day - passed_colder_day
            warmer_days_stack.append(day)
        return answer
        