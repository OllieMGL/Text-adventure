import time 
from classes.player import Player
import classes.Item as Item
import utils.input_handling as input_handler
from data.locations import init_locations 

   

CAN_ATTACK_ACTIONS = ["attack", "grab", "drop", "heal"]

starting_loc = init_locations() 

#init player
player = Player(100, [], starting_loc )

 
def handleUserInput(user_input):
    words = user_input.strip().lower().split(" ")
    verb = words[0]
    if verb == "attack":
        input_handler.attack(player, words)
    elif verb == "heal":
        input_handler.heal(player, words)
    elif verb == "look":
        input_handler.look(player, words)
    elif verb == "go":
        input_handler.go(player, words)
    elif verb == "directions":
        input_handler.getDirections(player)
    elif verb == "grab":
        input_handler.grab(player, words)
    elif verb == "inventory":
        player.printInventory()
    elif verb == "drop":
        player.dropItem(words[1].lower())
    elif verb == "die":
        input_handler.die(player)
    elif verb == "health" or verb == "vitals":
        print(f"Player health is {player.health}")
    elif verb == "help":
        input_handler.helpList(player)
    else:
        print("I did not understand that")

    #Now that player has had action, check if any enemies can attack
    if verb in CAN_ATTACK_ACTIONS:
        player.current_location.setCanAttack(True)


print("Welcome to The Knights of the Square Table...")
print(player.current_location.description)

while player.health > 0:
    handleUserInput(input(">>> "))
    if player.current_location.can_attack == True:
        player.current_location.enemiesAttack(player)
        


time.sleep(3)
print("You died.dumy")