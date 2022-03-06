import time 
from location import Location
from descriptions import descriptions


hut = Location(descriptions["hut"], "hay", "bye")


# global variables
current_location = hut 


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
    elif verb== "teleport":
        #Testing purpose teleport to new location
        spaceship = Location(descriptions["spaceship"],"test","test")
        global current_location 
        current_location = spaceship
        print("YOu teleported!")
    else:
        print("I did not understand that")
        
        
def attack(words):
    print("doin a attack")
    
def heal(words):
    print("doin a heal")
    
def look(words):
     print(current_location.description)
        
def go(words):
     print()        
    
    


print("Welcome to Skyrim but easy...")

while True: 
    handleUserInput(input(">>> "))