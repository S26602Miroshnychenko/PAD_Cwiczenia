Male = "Male"
Female = "Female"

class Animal:
    isAlive = True
    gender = "Female"
    genus = None

    def __init__(self, gender="Female", genus=None):
        self.gender = gender
        self.genus = genus

    def breed(self, partner):
        try:
            if self.gender == "Female" and partner.gender == "Male" and self.genus == partner.genus:
                if self.genus == "Canis":
                    return Dog(Male)
                else:
                    return Cat(Female)
        except:
            print("attribute not found")

class Dog(Animal):
    def __init__(self, gender):
        super().__init__(gender, genus="Canis")
    def woof(self):
        return "woof woof"

class Cat(Animal):
    def __init__(self, gender):
        super().__init__(gender, genus="Feis")
    def purr(self):
        return "purr"

Dogi = Dog(Male)
Dogj = Dog(Female)
Cati = Cat(Female)
Catj = Cat(Male)
szczeniak_dog = Dogj.breed(Dogi)
szczeniak_cat = Cati.breed(Catj)
print(szczeniak_dog.woof())
