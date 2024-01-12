# talking about classes and objects

class Superhero:
    # You want to always start with __init__ in order to initialize the class
    # self is the first parameter of __init__
    base_rate = 1000
    def __init__(self, name, superpowers, villians_beaten):
        self.name = name
        self.superpower = superpowers
        self.villains_beaten = villians_beaten

    # You can create functions inside of classes
    def get_rate(self):
        superpower_bonus = len(self.superpower) * 1000
        # get the bonus for villians beaten
        villain_bonus = self.villains_beaten * 250
        calculated_rate = self.base_rate + superpower_bonus + villain_bonus
        # return the final rate
        return calculated_rate

    def describe(self):
        print("My name is " + self.name + " and I have " + str(len(self.superpower)) + " superpowers.")
        print(f"I have beaten {self.villains_beaten} villains.")#here is another way to type in the information by using f strings
        print(f"My rate is {self.get_rate}.")



hero1 = Superhero("Superman", ["flight", "super strength", "heat vision"], 100)
hero2 = Superhero("Batman", ["money", "cool"], 1)

print(hero1.get_rate)

print(hero2.describe())