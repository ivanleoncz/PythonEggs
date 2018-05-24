#!/usr/bin/python3
""" Demonstrating concepts of subclassing, multiple inheritance and MRO. """

class Family:

    def __init__(self):
        print("\nBuilding family member...")

    def family_name(self):
        return "The name of our family is Jacques."


class Daughter(Family):

    def __init__(self):
        Family.__init__(self)
        print("\nMy Daughter, The Ocelot, was born.")

    def family_origin(self):
        return "The origin of our family if from Mexico and Brazil."


class Son(Daughter, Family):

    def __init__(self):
        print("\n- method name/origin:", str(super().family_name).split()[2])
        print("- ouput:", super().family_name())
        print("\n- method name/origin:", str(super().family_origin).split()[2])
        print("- ouput:", super().family_origin())
        print("\nMy Son, The Jaguar, was born.")


Daughter()
Son()
