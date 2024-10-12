import math

class Entity:
    
    def __init__(self, position):
        #self.angle_position = math.atan2(position[0],position[1])/math.pi*180
        self.distance = math.dist(position, (0, 0))
        self.angle_position = math.atan2(position[0], position[1])
        self.position = position
        
    def update_position(self, position):
        #self.angle_position =  math.atan2(position[0],position[1])/math.pi*180
        self.distance = math.dist(position, (0, 0))
        self.angle_position = math.atan2(position[0], position[1])
    
    def get_position(self):
        return (50*math.cos(self.angle_position), 50*math.sin(self.angle_position))
