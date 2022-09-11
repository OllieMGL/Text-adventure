import time 
from location import Location
from descriptions import descriptions
from inventory import inventory
from player import Player
from enemy import Enemy
import Item
from NPC import Npc 


# init locations
hut = Location(descriptions["hut"], inventory["hut"], 
               enemies=[Enemy("Draugr", 20, 8), Enemy("Skeever", 5, 2),Enemy("Draugr", 30, 8)])
riften = Location(descriptions["riften"], inventory["riften"])
riften_swamp = Location(descriptions["riften_swamp"])
secret_cave = Location(descriptions["secret_cave"], inventory["cave"],
    enemies=[Enemy("Draugr", 20, 8), Enemy("Skeever", 5, 2)])
oasis = Location(descriptions["oasis"], inventory["oasis"],
    enemies = [Enemy("Troll", 50, 12)])
church = Location(descriptions["church"], inventory["church"],
    npcs = [Npc("Priest", 10, None, 5, 6)])
shop = Location(descriptions["shop"], inventory["shop"])  
church_vault = Location(descriptions["church_vault"], inventory["church_vault"],
    enemies = [Enemy("draugr", 20, 8)])



hut.setDirections({"outside": riften_swamp}) 
riften_swamp.setDirections({"inside": hut, "riften": riften, "cave": secret_cave})
riften.setDirections({"swamp": riften_swamp, "church": church, "shop": shop})
secret_cave.setDirections({"outside": riften_swamp, "inside": oasis})
oasis.setDirections({"outside": secret_cave, "up": church})
church.setDirections({"down": oasis, "outside": riften,"inside": church_vault })
shop.setDirections({"outside": riften})
church_vault.setDirections({"outside" : church})


#init player
player = Player(100, [], hut )

 


def handleUserInput(user_input):
    words = user_input.strip().lower().split(" ")
    verb = words[0]
    if verb == "attack":
        attack(words)
    elif verb == "heal":
        heal(words)
    elif verb == "look":
        look(words)
    elif verb == "go":
        go(words)
    elif verb == "directions":
        getDirections()
    elif verb == "grab":
        grab(words)
    elif verb == "inventory":
        player.printInventory()
    elif verb == "drop":
        player.dropItem(words[1].lower())
    elif verb == "die":
        die()
    elif verb == "help":
        helpList()
    else:
        print("I did not understand that")
        
def grab(words):
    if " ".join(words[1:]).lower() in player.current_location.getInventoryLower():
        player.addItemToInventory(player.current_location.grabItem(" ".join(words[1:]).lower()))
        print(f"{' '.join(words[1:])} taken")
    else:
        print("No item in area")


 # finish off                        
def die():
    player.health = 0
    # #if you have a blade:
    #     time.sleep(1)
    #     print("You pulled your balde out and held it solemly in your hands...")
    #     time.sleep(2.5)
    #     print("You got your knees ready to slice your stomach with the balde meant for others rather than your own...")
    #     time.sleep(2.9)
    #     print("You sliced your stomach open, blood rushing from your wound...")
    #     time.sleep(2.8)
    #     print("You fall to the ground and perish, but only with one regret...")
    #     time.sleep(3)
    #     print("You left the stove on.")

    # else:
    #     print("You picked up a stone on the ground")    
        
        
def attack(words):
    if len(words) < 2:
        print("attack what bro")
        return
    
    target = None
    #checking if enemy is there
    for enemy in player.current_location.enemies:
        if enemy.name.lower() == words[1].lower():
            target = enemy
            break      
    if target != None:
        target.takeDamage(10)
        if target.health <= 0:
            player.current_location.enemies.remove(target)
    
    else: 
        print(f"No enemy named {words[1]}")
        print("You flung the air with style and destroyed the air particles.")
    
def heal(words):
    print("doin a heal")
    
def look(words):

    if len(words) > 2 and words[1] == "at":
        player.lookAtItem(" ".join(words[2:]))

    else:    
        #Location description
        print(f"\n{player.current_location.description}")
        
        #Items
        print("\nItems:")
        if len(player.current_location.inventory) > 0:
            for item in player.current_location.inventory:
                print(f"- {item.name}")
        else:
            print("No items can be seen...")
        
        #Enemies
        
        if len(player.current_location.enemies) > 0:
            print("\nEnemies:")
            for enemy in player.current_location.enemies:
                enemy.toString()

        if len(player.current_location.npc) > 0:
            print("People in area:")
            for i in player.current_location.npc:
                i.toString()
        
def go(words):
    direction = words[1]
    if direction in player.current_location.directions.keys():
        player.current_location = player.current_location.directions[direction]
        look(words)
    
    else:
        print("That is not a location you can go to, try these instead:")
        print(list(player.current_location.directions.keys()))
            
       
def getDirections():
    print(list(player.current_location.directions.keys()))
    
def helpList():
    player.helpFunction()


print("Welcome to Skyrim but easy...")

while player.health > 0:
    handleUserInput(input(">>> "))

time.sleep(3)
print("You died.dumy")