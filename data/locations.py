from classes.location import Location
from data.descriptions import descriptions
from data.inventory import inventory
from classes.enemy import Enemy
import classes.Item as Item
from classes.NPC import Npc


def init_locations():


#Create location objetcs

    hut = Location(
        name = descriptions["hut"]["name"],
        description = descriptions["hut"]["description"],
        inventory   = inventory["hut"], 
        enemies     =[
            Enemy("Draugr", 20, 8, Item.Item("Draugr Claws", 35, 1)),
            Enemy("Skeever", 5, 2, Item.Item("Tail", 10, 1))
            ]
        )
    riften = Location(
        name = descriptions["riften"]["name"],
        description = descriptions["riften"]["description"],
        inventory   = inventory["riften"]
        )

    riften_swamp = Location(
        name = descriptions["riften_swamp"]["name"],
        description = descriptions["riften_swamp"]["description"]
        )

    secret_cave = Location(
        name = descriptions["secret_cave"]["name"],
        description = descriptions["secret_cave"]["description"],
        inventory   = inventory["cave"],
        enemies=[
            Enemy("Draugr", 20, 8, "Draugr Head"),
            Enemy("Skeever", 5, 2, "Skeever Tail")
            ]
        )

    oasis = Location(
        name = descriptions["oasis"]["name"],
        description = descriptions["oasis"]["description"],
        inventory   =  inventory["oasis"],
        enemies     = [
            Enemy("Troll", 50, 12, "Troll Fat")
            ]
        )

    church = Location(
        name = descriptions["church"]["name"],
        description = descriptions["church"]["description"],
        inventory   = inventory["church"],
        npcs        = [Npc("Priest", 10, None, 5, 6)]
        )

    shop = Location(
        name = descriptions["shop"]["name"],
        description = descriptions["shop"]["description"],
        inventory   = inventory["shop"]
        )

    church_vault = Location(
        name = descriptions["church_vault"]["name"],
        description = descriptions["church_vault"]["description"],
        inventory   = inventory["church_vault"],
        enemies     = [
            Enemy("draugr", 20, 8, "draugr teeth")
            ]
        )


#Set paths that can be taken from each location 

    hut.setInitialDirections({
        "outside": riften_swamp
        })

    riften_swamp.setInitialDirections({
        "inside": hut,
        "riften": riften,
        "cave": secret_cave
        })

    riften.setInitialDirections({
        "swamp": riften_swamp,
        "church": church,
        "shop": shop
        })

    secret_cave.setInitialDirections({
        "outside": riften_swamp,
        "inside": oasis
        })

    oasis.setInitialDirections({
        "outside": secret_cave,
        "up": church
        })

    church.setInitialDirections({
        "down": oasis,
        "outside": riften,
        "inside": church_vault
         })

    shop.setInitialDirections({
        "outside": riften
        })

    church_vault.setInitialDirections({
        "outside" : church
        })

    return  [hut, riften_swamp, riften, secret_cave, oasis, church, shop, church_vault]