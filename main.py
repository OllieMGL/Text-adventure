import time 
from classes.player import Player
import classes.Item as Item
import utils.input_handling as input_handler
from data.locations import init_locations 

   

CAN_ATTACK_ACTIONS = ["attack", "grab", "drop", "heal"]

locations = init_locations()

#init player
# player = Player(100, [], locations[0])
player = Player(100, [], locations[0])


 
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
    elif verb == "quit":
        input_handler.quit()    
    else:
        print("I did not understand that")

    #Now that player has had action, check if any enemies can attack
    if verb in CAN_ATTACK_ACTIONS:
        player.current_location.setCanAttack(True)

def enemies_exist():
    total_enemies = 0
    for location in locations:
        total_enemies = total_enemies + len(location.enemies)
    if total_enemies > 0:
        print(f"{total_enemies} enemies remaining...")
        return True
    return False


def play(player):
    print("Welcome to TBAG...")
    print(player.current_location.description)
    time.sleep(2)
    print("On the floor you see a bleached parchment with large letters enscribed.")
    time.sleep(2)
    print("It reads, 'vanquish every foe to claim victory.'")
    time.sleep(2)
    print("You drop the paper and realize your goal.")


    while player.health > 0:
        handleUserInput(input(">>> "))
        if player.current_location.can_attack == True:
            player.current_location.enemiesAttack(player)
        
        # check win con
        if not enemies_exist():
            print("You win!")
            break

    time.sleep(3)
    if player.health < 1:
        print("You died.dumy")
    replay = input('would you like to replay?')
    if replay == 'yes':
        player.reset()
        for location in locations:
            location.reset()

        play(player)


play(player)