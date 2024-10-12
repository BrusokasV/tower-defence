import random
import math
from entity import Entity

class Enemies(Entity):
    def __init__(self, position):
        super().__init__(position)  
        self.hit = 0
        self.spawn_status = False
        self.taken_life = False


    def set_hit(self, mult):
        self.hit*=mult

    def get_hit(self):
        return self.hit
    
    def set_spawned(self, spawn_status):
         self.spawn_status = spawn_status

    def set_taken_life(self, taken_life):
        self.taken_life = taken_life

    def get_taken_life(self):
        return self.taken_life





def spawn_enemy():
        spawn_distance = 500
        choice = [3, 5, 6]
        position = random.randint(0, 100)  # You can define how position works
        new_enemy = Enemies((spawn_distance*math.sin((2*math.pi/100)*position), spawn_distance*math.cos((2*math.pi/100)*position)))  # Create a new enemy with a random position
        new_enemy.hit = choice[random.randint(0, 2)]  # Set the hit value (1-10)
        return(new_enemy)

# Populate enemies with a pause between spawning
def populate(enemies_array):

    max_enemies = 100  # Set maximum number of enemies to spawn

    while len(enemies_array) < max_enemies:
        enemies_array.append(spawn_enemy())
        
