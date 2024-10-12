import math
class User:
    score = 0
    lives = 3
    
    def __init__(self, position):
        self.angle_position = math.atan2(position[0],position[1])/math.pi*180
        self.distance = 1 #for now
        
    def update_position(self, position):
        self.angle_position =  math.atan2(position[0],position[1])/math.pi*180
    
    def get_position(self):
        return self.angle_position
    
    def reduce_lives(self):
        self.lives-=1
    
    def add_score(self, score):
        self.score+=score
    