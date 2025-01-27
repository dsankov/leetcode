class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        is_prerequisite = [[False] * numCourses for _ in range(numCourses)]
        for u, v in prerequisites:
            is_prerequisite[u][v] = True

        for intermediate in range(numCourses):
            for src in range(numCourses):
                for target in range(numCourses):
                    is_prerequisite[src][target] |= (is_prerequisite[src][intermediate] 
                                                    and is_prerequisite[intermediate][target]
                                                    )

        result = []
        for u, v in queries:
            result.append(is_prerequisite[u][v])

        return result