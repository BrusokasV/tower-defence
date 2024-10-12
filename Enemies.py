import Entity
class Enemies(Entity):
    
    def __init__(self,position, distance, hit):
        super(Entity, self).__init__(position, distance)
        self.hit = hit
    