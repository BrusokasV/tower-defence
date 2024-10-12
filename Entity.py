import math

class Entity:
    
    def __init__(self, position, distance):
        self.angle_position = math.atan2(position[0],position[1])/math.pi*180
        self.distance = distance
        
    def update_position(self, position):
        self.angle_position =  math.atan2(position[0],position[1])/math.pi*180
    
    def get_position(self):
        return self.angle_position