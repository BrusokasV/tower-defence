import Entity
class Enemies(Entity):
    
    def __init__(self,position):
        super(Entity, self).__init__(position)
        self.hit = 0
        
        