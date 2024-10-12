import random
import time
import math

class Enemies(Entity):
    def _init_(self, position):
        super()._init_(position)  # Call the parent constructor
        self.hit = 0  # Initialize hit

# Array to store enemies
enemies_array = []

# Function to spawn enemies
def spawn_enemy(enemy_list, enemy_count):
    for _ in range(enemy_count):
        # Assuming enemies need a position, random position can be added here
        position = random.randint(0, 100)  # You can define how position works
        new_enemy = Enemies(position)  # Create a new enemy with a random position
        new_enemy.hit = random.randint(1, 10)  # Set the hit value (1-10)
        enemy_list.append(new_enemy)

# Populate enemies with a pause between spawning
def populate():
    enemy_count = 1  # Start with 1 enemy
    max_enemies = 100  # Set maximum number of enemies to spawn

    while len(enemies_array) < max_enemies:
        spawn_enemy(enemies_array, enemy_count)  # Spawn enemies
        print(f"Spawned {enemy_count} new enemies. Total: {len(enemies_array)}")
        
        for enemy in enemies_array:
            print(f"Enemy at position {enemy.position} with hit {enemy.hit}")
        
        enemy_count += 1  # Increment the number of enemies to spawn each time
        time.sleep(5)  # Pause for 5 seconds before next spawn

# Placeholder for your main function
if _name_ == "_main_":
    populate()