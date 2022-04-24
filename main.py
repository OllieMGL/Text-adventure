import time 
from location import Location
from descriptions import descriptions
from inventory import inventory
from player import Player

# init locations
hut = Location(descriptions["hut"], inventory["hut"])
riften = Location(descriptions["riften"], inventory["riften"])
riften_swamp = Location(descriptions["riften_swamp"], None)
secret_cave = Location(descriptions["secret_cave"], inventory["cave"])

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
    else:
        print("I did not understand that")
        
def grab(words):
    if words[1].lower() in player.current_location.inventory:
        player.addItemToInventory(words[1])
        player.current_location.inventory.remove(words[1])
        print(f"{words[1]} taken")
    else:
        print("No item in area")
                         
        
        
        
def attack(words):
    print("doin a attack")
    
def heal(words):
    print("doin a heal")
    
def look(words):
    print(f"\n{player.current_location.description}")
    print("\nItems:")
    if player.current_location.inventory is not None:
        for item in player.current_location.inventory:
            print(f"- {item}")
    else:
        print("No items can be seen...")
        
def go(words):
    direction = words[1]
    player.current_location = player.current_location.directions[direction]

    
def getDirections():
    print(list(player.current_location.directions.keys()))


print("Welcome to Skyrim but easy...")

while True:
    handleUserInput(input(">>> "))