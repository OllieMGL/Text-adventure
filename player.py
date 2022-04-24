class Player:
    #health
    #inventory
    #current location
    
    def __init__ (self, health, inventory, location):
        self.health = health
        self.inventory = inventory
        self.current_location = location
        
        
    def addItemToInventory(self, item):
        self.inventory.append(item)

    def dropItem(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"dropped {item}")
            self.current_location.inventory.append(item)
        else:
            print(f"{item} not in inventory")
        