class User:
    def __init__(self, userName):
        self.name = userName

class Dog:
    def __init__(self, name, ownerName):
        #TOY ATTRIBUTES GO HERE (inside_init_function)
        print("_init_function has run!")
        self.name = name
        self.owner = User(ownerName)

    def bark(self):
        print(self.name)

    def play(self, toy):
        print(self.name + "loves to play with his" + toy)

    def lick(self, other_pet):
        print(self.name + "has licked" + other_pet.name)

    def owner_info(self):
        print(self.name + "'s owner is" + self.owner.name)

    #TOY METHODS GO HERE(inside class)

odie = Dog("Odie","jon")
pluto = Dog("Pluto", "george")
snoopy = Dog("Snoopy", "bob")
odie.owner_info()