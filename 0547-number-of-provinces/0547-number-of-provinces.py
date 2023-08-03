class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        if n <= 1:
            return n

        provinces = [{i} for i in range(n)]
        for city_a in range(n):
            for city_b in range(city_a, n):
                if isConnected[city_a][city_b]:
                    provinces[city_a].update(provinces[city_b])
                    for neighbour in provinces[city_a]:
                        provinces[neighbour] = provinces[city_a]
        
        return len(set(frozenset(province) for province in provinces))


