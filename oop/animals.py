

class Animal:

    def eat(self):
        return "eating"

    def drink(self):
        return "drinking"

    def sleep(self):
        return "sleeping"

    def procreate(self):
        return "procreating"


class Eagle(Animal):

    __huntCounter = 0
    __eatCounter = 0

    def fly(self):
        return "flying"

    def hunt(self):
        self.__huntCounter += 1
        self.__eatCounter += 1
        return "hunting (counter: %s)" % self.__huntCounter

    # overridden method
    def eat(self):
        if self.__huntCounter == 0:
            return "Have you hunted lately?"
        else:
            self.__eatCounter -= 1
            self.__huntCounter -= 1
            return "Eating snakes! Remaining snakes: %s" % self.__eatCounter

    # overridden method
    def drink(self):
        return "drinking water"

    # overridden method
    def sleep(self):
        return "sleeping on the mountain"

    # overridden method
    def procreate(self):
        return "procreating on the nest"


class Catle(Animal):


    def wander(self):
        return "wandering"

    def graze(self):
        return "grazing"

    # overridden method
    def eat(self):
        return "eating grasslands"

    # overridden method
    def drink(self):
        self.__drinkCounter += 1
        return "drinking water"

    # overridden method
    def sleep(self):
        self.__sleepCounter += 1
        return "sleeping on the farm"

    # overridden method
    def procreate(self):
        self.__procreateCounter += 1
        return "procreating on the grass"
