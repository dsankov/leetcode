class Solution:
    def maxProfitAssignment(self, difficulties: List[int], profits: List[int], workers: List[int]) -> int:
        jobs = defaultdict(lambda: inf)
        for i, profit in enumerate(profits):
            jobs[profit] = min(jobs[profit], difficulties[i]) 
        jobs = sorted(jobs.items(), reverse=True)
        workers.sort(reverse=True)

        job = 0
        worker = 0
        result = 0
        while worker < len(workers) and job < len(jobs):
            if workers[worker] >= jobs[job][1]:
                result += jobs[job][0]
                worker += 1
            else:
                job += 1
        return result