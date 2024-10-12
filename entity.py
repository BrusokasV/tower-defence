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

    def set_distance(self, distance):
        self.distance = distance
    
    def get_position(self):
        return (self.distance*math.sin(self.angle_position), self.distance*math.cos(self.angle_position))
    
    def get_angle_pos(self):
        return self.angle_position
    
    def get_distance(self):
        return self.distance
