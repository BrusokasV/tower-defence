import math
class User:
    
    def __init__(self, x_pos, y_pos):
        self.angle_position = math.atan2(x_pos,y_pos)/math.pi*180
        self.distance = 1 #for now
        
    