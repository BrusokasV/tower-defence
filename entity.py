import math, main

class Entity:
    
    def __init__(self, position):
        self.angle_position = math.atan2(position[0],position[1])/math.pi*180
        self.distance = math.dist(position, [main.dimension_x/2, main.dimension_y/2])
        
    def update_position(self, position):
        self.angle_position =  math.atan2(position[0],position[1])/math.pi*180
    
    def get_position(self):
        return self.angle_position
