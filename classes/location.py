class Location:
    #ATTRIBUTES
    #description - Str
    #inventory - list
    #directions - dict
    #enemies - list
    #can_attack - bool
    
    def __init__(self, description, inventory=[], enemies=[], npcs=[]):

        self.description = description
        self.inventory = inventory
        self.enemies = enemies
        self.npc = npcs
        self.can_attack = False
    
    #Set the directions attribute of the object
    def setDirections(self, directions: 'dict'):
        self.directions = directions

    def getInventoryLower(self):
        inventory = []
        for item in self.inventory:
            inventory.append(item.name.lower())
        return(inventory)
    
    def grabItem(self, nameLower):
        for item in self.inventory:
            if nameLower == item.name.lower():
                #I've got the item which name is equal to user input -> item
                self.inventory.remove(item)
                return(item)

    def setCanAttack(self, canAttack):
        self.can_attack = canAttack

    def enemiesAttack(self, player):
        for enemy in self.enemies:
            enemy.attack(player)
        self.setCanAttack(False)