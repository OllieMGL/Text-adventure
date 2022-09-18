class Enemy:
    '''
    ATTRIBUTES
    name -string
    health - int
    power - int
    '''
    
    def __init__ (self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        
    def toString(self):
        print(f"- {self.name}, {self.health} health")
        
    def takeDamage(self, amount):
        print(f"You attacked {self.name} for {amount}")
        self.health = self.health - amount
    
    def attack(self, player):
        player.takeDamage(self.power)
        print(f"{self.name} attacks you for {self.power} damage!")