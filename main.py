import time 
from location import Location
from descriptions import descriptions
from inventory import inventory
from player import Player
from enemy import Enemy

# init locations
hut = Location(descriptions["hut"], inventory["hut"], 
               enemies=[Enemy("Draugr", 20, 8), Enemy("Skeever", 5, 2),Enemy("Draugr", 30, 8)])
riften = Location(descriptions["riften"], inventory["riften"])
riften_swamp = Location(descriptions["riften_swamp"])
secret_cave = Location(
    inventory=inventory["cave"],
    description=descriptions["secret_cave"], 
    enemies=[Enemy("Draugr", 20, 8), Enemy("Skeever", 5, 2)]
    )

hut.setDirections({"outside": riften_swamp}) 
riften_swamp.setDirections({"inside": hut, "riften": riften, "cave": secret_cave})
riften.setDirections({"swamp": riften_swamp})
secret_cave.setDirections({"outside": riften_swamp})

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
        print(player.inventory)
    elif verb == "drop":
        player.dropItem(words[1].lower())
    elif verb == "die":
        die()
    elif verb == "help":
        helpList()
    else:
        print("I did not understand that")
        
def grab(words):
    if words[1].lower() in player.current_location.inventory:
        player.addItemToInventory(words[1])
        player.current_location.inventory.remove(words[1])
        print(f"{words[1]} taken")
    else:
        print("No item in area")
                         
def die():
    player.health = 0
        
        
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
    #Location description
    print(f"\n{player.current_location.description}")
    
    #Items
    print("\nItems:")
    if len(player.current_location.inventory) > 0:
        for item in player.current_location.inventory:
            print(f"- {item}")
    else:
        print("No items can be seen...")
    
    #Enemies
    
    if len(player.current_location.enemies) > 0:
        print("\nEnemies:")
        for enemy in player.current_location.enemies:
            enemy.toString()

        
def go(words):
    direction = words[1]
    if direction in player.current_location.directions.keys():
        player.current_location = player.current_location.directions[direction]
        print(f"\n{player.current_location.description}")

        print("\nItems:")
        if len(player.current_location.inventory) > 0:
            for item in player.current_location.inventory:
                print(f"- {item}")
        else:
            print("No items can be seen...")
    
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

print("You died.dumy")