class Player:
    #health
    #inventory
    #current location
    
    def __init__ (self, health: 'int', inventory: 'list', location: 'Location'):
        self.health = health
        self.inventory = inventory
        self.current_location = location
        
        
    def addItemToInventory(self, item):
        self.inventory.append(item)

    #Remove item from inventory and add back to inventory of current location
    def dropItem(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"dropped {item}")
            self.current_location.inventory.append(item)
        else:
            print(f"{item} not in inventory")
        