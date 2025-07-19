import random

class Box:
    def __init__(self, color):
        self.color = color

class ConveyorSystem:
    def __init__(self, allowed_color="green"):
        self.allowed_color = allowed_color
        self.current_box = None

    def generate_box(self):
        color = random.choice(["red", "green", "blue"])
        self.current_box = Box(color)
        return self.current_box

    def check_box(self):
        if self.current_box.color == self.allowed_color:
            return "pass"
        else:
            return "reject"
