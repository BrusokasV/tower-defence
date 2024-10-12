import math, Entity
class User(Entity):
    score = 0
    lives = 3
    
    def __init__(self, position):
        super(Entity, self).__init__(position)
        self.distance = 1
        
    
    def reduce_lives(self):
        self.lives-=1
    
    def add_score(self, score):
        self.score+=score
    