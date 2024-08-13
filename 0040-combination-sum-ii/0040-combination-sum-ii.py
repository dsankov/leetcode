class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.candidates = candidates
        self.n = len(candidates)
        self.target = target
        
        self.candidates.sort()
        self.backtrack(start_index=0, current_path=[], current_target=target)
        return self.result

    def backtrack(self, start_index, current_path, current_target):
        if current_target == 0:
            self.result.append(current_path)
            return
        for i in range(start_index, self.n):
            if i > start_index and self.candidates[i] == self.candidates[i-1]:
                continue
            if self.candidates[i] > current_target:
                return
            self.backtrack(
                start_index=i+1, 
                current_path=current_path+[self.candidates[i]],
                current_target=current_target-self.candidates[i]
                )