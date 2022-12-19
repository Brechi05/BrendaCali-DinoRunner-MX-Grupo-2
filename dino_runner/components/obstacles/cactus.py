from dino_runner.components.obstacles.obstacle import Obstacle
import random

class Cactus(Obstacle): # hereda de obs
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
 