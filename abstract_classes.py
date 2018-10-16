#!/usr/bin/python3

from abc import ABC, abstractmethod

class Body(ABC):

    def __init__(self):
        print("\nBuilding Body!")

    @abstractmethod
    def parts(self):
        pass

    @abstractmethod
    def special_parts(self):
        pass


class Computer(ABC):

    def __init__(self):
        print("\nBuilding Computer!")

    @abstractmethod
    def commands(self):
        pass
        
    @staticmethod
    def special_commands():
        print("- adding special command: fly")
        print("- adding special command: levitate")
        print("- adding special command: defend")
        print("- adding special command: shoot")


class Robot(Body, Computer):

    def __init__(self, name):
        self.name = name
        print("Building robot:", self.name)

    def parts(self):    # abstract method from Body class
        Body.__init__(self)
        print("- adding part: trunk")
        print("- adding part: head")
        print("- adding part: arms")
        print("- adding part: legs")

    def special_parts(self):    # abstract method from Body class
        print("- adding special part: antenna")
        print("- adding special part: machine gun")
        print("- adding special part: shield")

    def commands(self):     # abstract method from Computer class
        Computer.__init__(self)
        print("- adding command: move left arm")
        print("- adding command: move left leg")
        print("- adding command: move right arm")
        print("- adding command: move right leg")
        print("- adding command: move head")


robot = Robot("James")
robot.parts()
robot.special_parts()
robot.commands()
robot.special_commands()

