class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(defaultdict)
        for (divisible, divisor), quotient in zip (equations, values):
           graph[divisible][divisor] = quotient
           graph[divisor][divisible] = 1 / quotient

        def dft(divisible, divisor, quotient, visited):
            if divisible not in graph or divisible in visited:
                return None
            if divisor == divisible:
                return quotient
            
            visited.add(divisible)
            for neighbour in graph[divisible]:
                row_result = dft(neighbour, divisor, quotient * graph[divisible][neighbour], visited)
                if row_result:
                    return row_result

            return None


        row_results = [dft(divisible, divisor, 1, set()) for (divisible, divisor) in queries]
        return [quotient if quotient else -1.0 for quotient in row_results]       

            
        