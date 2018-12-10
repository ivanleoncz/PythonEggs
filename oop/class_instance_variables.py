
class Shark:

    animal_type = "fish"
    location = "ocean"
    followers = 5

    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Shark("Frederick", 12)
s2 = Shark("Nicholas", "10")


print("\n>>> Shark 1 <<<")
print("Name:", s1.name)
print("Age:", s1.age)
print("Type:", s1.animal_type)
print("Location:", s1.location)
print("Followers:", s1.followers)


print("\n>>> Shark 2 <<<")
print("Name:", s2.name)
print("Age:", s2.age)
print("Type:", s2.animal_type)
print("Location:", s2.location)
print("Followers:", s2.followers)

