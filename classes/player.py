from classes.Item import *

class Player:
    #health
    #inventory (list of Item object)
    #current location
    
    def __init__ (self, health: 'int', inventory: 'list', location: 'Location'):
        self.health = health
        self.inventory = inventory
        self.current_location = location
        
        
    def addItemToInventory(self, item):
        self.inventory.append(item)

    #Remove item from inventory and add back to inventory of current location
    def dropItem(self, itemName: 'str'):
        for item in self.inventory:
            if itemName == item.name.lower():
                self.inventory.remove(item)
                print(f"dropped {item.name}")
                self.current_location.inventory.append(item)
            else:
                print(f"{item.name} not in inventory")


    def lookAtItem(self, itemName):
        not_found = True
        for item in self.inventory:
            if itemName.lower() == item.name.lower():
                not_found = False
                item.lookAt()
        if not_found:
            print(f"You do not have {itemName}")

    def printInventory(self):
        if len(self.inventory) > 0:
            for i in self.inventory:
                print(f"- {i.name}")
        else:
            print("You have nothing in your inventory")        

    # def setHealth(self, new_health):
    #     self.health = new_health
    
    def takeDamage(self, damage: 'int'):
        self.health = self.health - damage


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
                      "look at - to inspect an item and see its attirbutes"
                      "Die - to... well... die"
                     ]
        print("\fHA you need help. Maybe see if you can try and use these words:")
        print("")
        for i in list_verbs:
            print(f"~~ {i}")
            
        print("//////////////////////////////////////////////////////////////////////////////")    
            
            
        
        
 