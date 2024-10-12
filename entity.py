import math

class Entity:
    
    def __init__(self, position, origin):
        self.angle_position = math.atan2(position[0],position[1])/math.pi*180
        self.distance = math.dist(position, origin)
        self.position = position
        
    def update_position(self, position):
        self.angle_position =  math.atan2(position[0],position[1])/math.pi*180
    
    def get_position(self):
        return self.position
