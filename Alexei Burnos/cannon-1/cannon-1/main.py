from scene import *
import ui
from math import pi
from constants import CANNON_FILENAME, CANNON_WHEEL_FILENAME


class MyScene(Scene):
    def __init__(self):
        self.background_color = 'lightblue'
        self.cannon = None
        self.wheel = None

    def setup(self):
        self.background_color = 'lightblue'
        self.wheel = SpriteNode(CANNON_WHEEL_FILENAME)
        self.wheel.position = (100, 100)
        self.wheel.size = (150, 220)
        self.add_child(self.wheel)
            
        self.cannon = SpriteNode(CANNON_FILENAME)
        self.cannon.position = (100, 100)
        self.cannon.size = (150, 220)
            
        self.cannon.rotation = - pi / 8
            
        self.add_child(self.cannon)


if __name__ == "__main__":
    run(MyScene())

