from classes.Item import Item

class Enemy:
    '''
    ATTRIBUTES
    name -string
    health - int
    power - int
    inventory - [Item.Item]
    '''
    
    def __init__ (self, name: str, health: int, power: int, inventory: [Item]):
        self.name = name
        self.health = health
        self.power = power
        self.inventory = inventory 
        
    def toString(self):
        print(f"- {self.name}, {self.health} health")
        
    def takeDamage(self, amount):
        print(f"You attacked {self.name} for {amount}")
        self.health = self.health - amount
    
    def attack(self, player):
        player.takeDamage(self.power)
        print(f"{self.name} attacks you for {self.power} damage!")