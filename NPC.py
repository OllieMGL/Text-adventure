class Npc: 
    def __init__(self, name, health, speech, gold, damage):
        self.name = name
        self.health = health    
        self.speech = speech
        self.gold = gold
        self.damage = damage

    def toString(self):
        print(f"- {self.name}, {self.health} health")
      

