import random
import time
import Entity

class Enemies(Entity):
    def _init_(self, position):
        super()._init_(position)  
        self.hit = 0  





def spawn_enemy():
    
        position = random.randint(0, 100)  # You can define how position works
        new_enemy = Enemies(position)  # Create a new enemy with a random position
        new_enemy.hit = random.randint(1, 10)  # Set the hit value (1-10)
        return(new_enemy)

# Populate enemies with a pause between spawning
def populate(enemies_array):

    max_enemies = 100  # Set maximum number of enemies to spawn

    while len(enemies_array) < max_enemies:
        enemies_array.append(spawn_enemy())
        
        time.sleep(5)  # Pause for 5 seconds before next spawn
    
