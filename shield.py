import math
from entity import Entity

class Shield(Entity):
    score = 0
    lives = 3
    
    def __init__(self, position, origin):
        super().__init__(position, origin)
        self.distance = 1
        
    
    def reduce_lives(self):
        self.lives-=1
    
    def add_score(self, score):
        self.score+=score
    