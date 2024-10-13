import math
from entity import Entity

class Shield(Entity):
    score = 0
    lives = 3
    shield_distance = 50
    high_score = 0
    
    def __init__(self, position, radius):
        super().__init__(position)
        self.distance = 1
        self.shield_distance = radius
        
    
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

    def reset_state(self):
        self.score = 0
        self.lives = 3
    def update_high_score(self):
        if self.score > Shield.high_score:
            Shield.high_score = self.score

    def get_high_score(self):
        return Shield.high_score