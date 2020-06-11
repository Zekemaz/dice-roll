# Creating class object
import random


class Dice:
    def __init__(self, _shape, _faces):
        self.shape = _shape
        self.faces = _faces

    def roll_dice(self):
        roll = random.randint(0, self.faces)
        return roll
