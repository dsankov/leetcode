class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        WHITE, GRAY, BLACK = range(3)
        vertices = {}
        adjacency_list = defaultdict(set)
        for u, v in prerequisites:
            vertices[u] = WHITE
            vertices[v] = WHITE
            adjacency_list[u].add(v)
        
        def is_cycle(vertex):
            if vertices[vertex] == GRAY:
                return True
            if vertices[vertex] == BLACK:
                return False

            vertices[vertex] = GRAY
            for neighbor in iter(adjacency_list[vertex]):
                if is_cycle(neighbor):
                    return True
            vertices[vertex] = BLACK
            return False


        for vertex in vertices: 
            if vertices[vertex] == WHITE:
                if is_cycle(vertex):
                    return False

        return True
        