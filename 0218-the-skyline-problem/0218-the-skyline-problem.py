class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        result = []        
        def add_to_result(x, height):
            if not result:
                result.append([x, height])
            else:
                last_x, last_height = result[-1]
                if x == last_x:
                    result.pop()
                    add_to_result(x, height)
                elif height != last_height:
                    result.append([x, height])

        events = []
        heights = [(0, -1)]
        current_height = 0
        ended_buildings = set()

        for building_index, (building_start, building_end, building_height) in enumerate(buildings):
            events.append((building_start, "start", building_index, building_height))
            events.append((building_end, "end", building_index, building_height))
        heapify(events)
        while events:
            building_edge, event_type, building_index, building_height = heappop(events)
            if event_type == "start":
                if building_height > current_height:
                    add_to_result(building_edge, building_height)
                    current_height = building_height
                negative_height = -building_height
                heappush(heights, (negative_height, building_index))
            else: # event_type == "end"
                ended_buildings.add(building_index)
                negative_active_building_height, active_building_index = heights[0]
                while active_building_index in ended_buildings:
                    heappop(heights)
                    negative_active_building_height, active_building_index = heights[0]
                active_building_height = -negative_active_building_height
                current_height = active_building_height
                add_to_result(building_edge, current_height)

        return result


