class Solution:
    def dividePlayers(self, skills: List[int]) -> int:
        n = len(skills)
        skills_sum = sum(skills)
        if skills_sum % (n // 2) != 0:
            return -1
        target_skill = skills_sum // (n // 2)
        skills_freq = Counter(skills)
        total_chemestry = 0
        for skill, freq in skills_freq.items():
            needed_skill = target_skill - skill
            if needed_skill not in skills_freq or skills_freq[needed_skill] != freq:
                return -1
            total_chemestry += skill * needed_skill * freq
        return total_chemestry // 2