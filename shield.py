import math
from entity import Entity

class Shield(Entity):
    score = 0
    lives = 3
    shield_distance = 50
    
    def __init__(self, position):
        super().__init__(position)
        self.distance = 1
        
    
    def reduce_lives(self):
        self.lives-=1

    def get_lives(self):
        return self.lives
    
    def add_score(self, score):
        self.score+=score
    
    def get_score(self):
        return self.score

    def get_position(self):
        return (self.shield_distance*math.sin(self.angle_position), self.shield_distance*math.cos(self.angle_position))