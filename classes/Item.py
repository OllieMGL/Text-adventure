class Item:

    def __init__ (self, name, value, amount):
        self.name = name
        self.value = value
        self.amount = amount

    def lookAt(self):
        print(f"~ Name - {self.name}")
        print(f"~ Value - {self.value}")


class Weapon(Item):
    def __init__(self, name, value, amount, damage):
        super().__init__(name, value, amount)
        self.damage = damage

    def lookAt(self):
         super().lookAt()
         print(f"~ Damage - {self.damage}")

class Potion(Item):
    def __init__(self, name, value, amount, type):
        super().__init__(name, value, amount)
        self.type = type

    def lookAt(self):
         super().lookAt()
         print(f"~ Type - {self.type}")
         print(f"~ Gain life - {self.amount}")     
    
    def use(self):
        print("restore health or something")