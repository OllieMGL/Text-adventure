import time 
from location import Location
from descriptions import descriptions
from inventory import inventory


hut = Location(descriptions["hut"], inventory["hut"])
riften = Location(descriptions["riften"], inventory["riften"])
riften_swamp = Location(descriptions["riften_swamp"], None)
secret_cave = Location(descriptions["secret_cave"], inventory["cave"])

hut.setDirections({"outside": riften_swamp}) 
riften_swamp.setDirections({"inside": hut, "riften": riften, "cave": secret_cave})
riften.setDirections({"swamp": riften_swamp})
secret_cave.setDirections({"outside": riften_swamp})




# global variables
current_location = hut 


def handleUserInput(user_input):
    print("\n")
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
    else:
        print("I did not understand that")
        
        
def attack(words):
    print("doin a attack")
    
def heal(words):
    print("doin a heal")
    
def look(words):
    print(current_location.description)
    print("\nItems:")
    for item in current_location.inventory:
        print(f"- {item}")
        
def go(words):
    direction = words[1]
    global current_location
    current_location = current_location.directions[direction]

    
def getDirections():
    print(list(current_location.directions.keys()))


print("Welcome to Skyrim but easy...")

while True:
    handleUserInput(input(">>> "))