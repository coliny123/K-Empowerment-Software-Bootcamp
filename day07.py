#10_10

class Laser:
    def does(self):
        return "disintegrate"
class Claw:
    def does(self):
        return "Crush"

class SmartPhone:
    def does(self):
        return "Ring"

class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()

    def does(self):
        return self.laser.does(), self.claw.does(), self.smartphone.does()

r = Robot()

print(r.does())