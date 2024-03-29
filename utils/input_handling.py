import classes.Item as Item
import time
import sys





def grab(player, words):
    if " ".join(words[1:]).lower() in player.current_location.getInventoryLower():
        player.addItemToInventory(player.current_location.grabItem(" ".join(words[1:]).lower()))
        print(f"{' '.join(words[1:])} taken")
    else:
        print("No item in area")


 # finish off                        
def die(player):
    player.health = 0

    for item in player.inventory:
        if isinstance(item, Item.Weapon) and item.name.lower() == 'sword':
            time.sleep(1.5)
            print("You pulled your balde out and held it solemly in your hands...")
            time.sleep(2)
            print("You got your knees ready to slice your stomach...")
            time.sleep(3)
            print("You sliced your stomach open, blood rushing from your wound...")
            time.sleep(2)
            print("You fall to the ground and perish, but only with one regret...")
            time.sleep(3)
            print("You left the stove on.")
            break

        
def attack(player, words):
    if len(words) < 2:
        print("attack what bro")
        return
    
    target = None
    #checking if enemy is there
    for enemy in player.current_location.enemies:
        if enemy.name.lower() == words[1].lower():
            target = enemy
            break
    
    damage = 5
    
    if len(words) > 3 and words[2] == "with":
        found_weapon = False

        for item in player.inventory:
            if isinstance(item, Item.Weapon) and item.name.lower() == words[3]:
                damage = item.damage
                found_weapon = True
                break

        if not found_weapon:
            print(f"You don't have {words[3]}")
                

    if target != None:
        target.takeDamage(damage)
        if target.health <= 0:
            player.current_location.enemies.remove(target)
            player.current_location.inventory.append(target.inventory)
            
    else: 
        print(f"No enemy named {words[1]}")
        print("You flung the air with style and destroyed the air particles.")
    
def heal(player, words):
    found_potion = ''
    if len(words) > 3 and words[1] == 'with':
        found_potion = False

        for item in player.inventory:
            if isinstance(item, Item.Potion) and item.name.lower() == (" ".join(words[2:]).lower()):
                player.gainhealth(item)

                found_potion = True
                player.inventory.remove(item)
                print(f'{item.name} broke after usage')
                break
         
    if found_potion == False:
        print(f'{(" ".join(words[2:]).lower())} is not in your inventory')

    if len(words) < 3:
        print('heal with what?')                 




def look(player, words):

    if len(words) > 2 and words[1] == "at":
        player.lookAtItem(" ".join(words[2:]))

    else:    
        #Location description
        print(f"\nYou are currrently in location {player.current_location.name}")
        time.sleep(2)
        print(f"{player.current_location.description}")
        
        #Items
        time.sleep(2)
        print("\nItems:")
        if len(player.current_location.inventory) > 0:
            for item in player.current_location.inventory:
                print(f"- {item.name}")
        else:
            print("No items can be seen...dingus")
        
        #Enemies
        
        if len(player.current_location.enemies) > 0:
            print("\nEnemies:")
            for enemy in player.current_location.enemies:
                enemy.toString()

        if len(player.current_location.npc) > 0:
            print("People in area:")
            for i in player.current_location.npc:
                i.toString()
        
def go(player, words):
    particles = ["in", "to", "up", "down"]
    if words[1] in particles and len(words)>2:
        if words[2] == "the":
            direction = words[3]
        else:
            direction = words[2]
    else:
        direction = words[1]
    if direction in player.current_location.directions.keys():
        player.current_location = player.current_location.directions[direction]
        look(player, words)
    
    else:
        print("That is not a location you can go to, try these instead:")
        print(list(player.current_location.directions.keys()))
            
       
def getDirections(player):
    print(list(player.current_location.directions.keys()))
    
def helpList(player):
    player.helpFunction()

def quit():
    user_input = input("Are you sure you would like to quit?(yes/no): ")
    if user_input == 'yes':
        print('Thank you for playing')
        sys.exit()
    else:
        print("Why did you say quit then dummo")    
