class Enemy:
    '''
    ATTRIBUTES
    health - int
    inventory - list
    directions - dict
    '''
    
    def __init__ (self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        
    def toString(self):
        print(f"- {self.name}, {self.health} health")
        