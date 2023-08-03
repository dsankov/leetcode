from collections import deque
class Solution:
    def get_neighbours(self, yx):
        neighbours = []
        if yx[0] >=1:
            neighbours.append((yx[0]-1, yx[1])) 
        if yx[0] < self.height:
            neighbours.append((yx[0]+1, yx[1])) 
        if yx[1] >=1:
            neighbours.append((yx[0], yx[1]-1)) 
        if yx[1] < self.width:
            neighbours.append((yx[0], yx[1]+1)) 
        return neighbours
    
    def get_color_at(self, point):
        return self.image[point[0]][point[1]]
    
    def set_color_at(self, point, color):
        self.image[point[0]][point[1]] = color
                
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        initial_color = image[sr][sc]
        queue_to_check = deque()
        queue_to_check.append((sr,sc))
        
        self.height = len(image) - 1
        self.width = len(image[0]) - 1
        self.image = image
        checked_points = set()
        
        while queue_to_check:
            point = queue_to_check.pop()
            print (f"testing point at: {point} with color: {self.get_color_at(point)}")
            self.set_color_at(point, color)
            checked_points.add(point)
            
            neighbours = self.get_neighbours(point)
            print (f"neighbours at: {point} are: {neighbours}")
            for neighbour in neighbours:
                if neighbour in checked_points:
                    continue
                if self.get_color_at(neighbour) == initial_color:
                    queue_to_check.append(neighbour)
                
        return self.image
            
            
            
        