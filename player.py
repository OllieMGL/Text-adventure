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
            
    def helpFunction(self):
        list_verbs = [
                      "Attack - to damage any enemy the player may come across",
                      "Heal - to gain back any lost health",
                      "Look - gain a description of your surrounding area",
                      "Go - to move yourself out the location",
                      "Directions - to see where you can move to",
                      "Grab - to add an item to your inventory",
                      "Inventory - to see what items you currently have in your inventory",
                      "Drop - to remove items from your inventory",
                      "Die - to... well... die"
                     ]
        print("\fHA you need help. Maybe see if you can try and use these words:")
        print("")
        for i in list_verbs:
            print(f"~~ {i}")
            
        print("//////////////////////////////////////////////////////////////////////////////")    
            
            
        
        
 