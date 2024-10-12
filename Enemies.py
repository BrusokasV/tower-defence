import random
import math
from entity import Entity

class Enemies(Entity):
    def __init__(self, position):
        super().__init__(position)  
        self.hit = 0
        self.spawn_status = False


    def set_hit(self, mult):
        self.hit*=mult

    def get_hit(self):
        return self.hit
    
    def set_spawned(self, spawn_status):
         self.spawn_status = spawn_status





def spawn_enemy():
        spawn_distance = 500
        position = random.randint(0, 100)  # You can define how position works
        new_enemy = Enemies((spawn_distance*math.sin((2*math.pi/100)*position), spawn_distance*math.cos((2*math.pi/100)*position)))  # Create a new enemy with a random position
        new_enemy.hit = random.randint(3, 7)  # Set the hit value (1-10)
        return(new_enemy)

# Populate enemies with a pause between spawning
def populate(enemies_array):

    max_enemies = 100  # Set maximum number of enemies to spawn

    while len(enemies_array) < max_enemies:
        enemies_array.append(spawn_enemy())
        
