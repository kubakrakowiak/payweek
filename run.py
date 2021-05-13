import names
import random
import readkeys

class Game:
    def __init__(self):
        self.time = 1000
        self.threat = 50
    def add_time(self, time):
        self.time += time
    def add_threat(self, threat):
        self.threat += threat

class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

class Player(Person):
    def __init__(self, name, lastname, cls):
        super().__init__(name, lastname)
        self.cls = cls

class Guard(Person):
    def __init__(self, name, lastname):
        super().__init__(name, lastname)
        self.power = random.randint(1, 60)

class Lock:
    def __init__(self):
        self.difficulty = random.randint(1,100)

class Gun:
    def __init__(self, name, ammo):
        self.name = name
        self.ammo = ammo







def main():
    #ch = readkeys.getch()
    First = Game()

    

    input()

if __name__ == "__main__":
    main()
