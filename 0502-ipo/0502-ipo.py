class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects_queue = []
        not_used_projects = set(range(n))
        new_projects = [i for i in not_used_projects if capital[i] <= w]
        
        not_used_projects.difference_update(new_projects)
        projects_queue.extend([-profits[i] for i in new_projects])
        heapify(projects_queue)
        while k > 0:
            if not projects_queue:
                break
            best_project = heappop(projects_queue)
            w += -best_project
            k -= 1
            new_projects = [i for i in not_used_projects if capital[i] <= w]
            if new_projects:
                not_used_projects.difference_update(new_projects)
                projects_queue.extend([-profits[i] for i in new_projects])
                heapify(projects_queue)
        return w
        