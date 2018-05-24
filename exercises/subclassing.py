class Machine:

    def __init__(self, project):
        self.project = project
        print("\nCreating Machine!\n\nProject Name:", self.project, "\n")

    def actions(self):
        print("Adding action to {0}: move forward".format(self.project))
        print("Adding action to {0}: move backward".format(self.project))
        print("Adding action to {0}: turn left".format(self.project))
        print("Adding action to {0}: turn right".format(self.project))


class Car(Machine):

    def __init__(self):
        super().__init__(self)
        print("Type: Car")
        super().actions()


m = Machine("Tesla")
m.actions()
