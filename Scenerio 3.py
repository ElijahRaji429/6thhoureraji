#Name: Elijah Raji
#Class:6th hour
#Assinment:scenerio 3

#Scenario 3:
#Now that the game development team has a dictionary for enemies
#(see Scenario 1) and the dictionary for the party is fixed
#(see Scenario 2), they want to start making a full prototype for the
#combat system. The team lead is a big Dungeons & Dragons fan and
#wants to make the combat similar to that. Because of this, the
#dictionaries need to be reworked slightly to be like that.

#Each enemy and party member in both dictionaries needs:
# - health points (somewhere between 6 and 25)
# - an attack modifier (somewhere between 3 and 7)
# - a damage roll (a number that varies based on weapon/spell)
# - and an Armor Class (somewhere between 10 and 17).

#Once both dictionaries are updated, create a combat
#prototype that has a party member attack first, then an enemy
#attacks back right after.

#To determine if a creature hits another creature, you roll a
#20-sided die (d20) and add the attack modifier to the roll.
#If that number is the same as or higher than the enemy's Armor Class
#(AC), the attack hits, and you roll for damage. If it is lower, the
#attack misses. If an enemy or party member hits zero (0) health
#points, they die.

#To make things easier, here is a reference list for party damage rolls.
#(Feel free to use similar numbers for your enemy dictionary.)

# - Lae'Zel uses a greatsword: 2d6 + 3
# - Shadowheart uses a mace: 1d6 + 2
# - Gale uses the firebolt spell: 1d10
# - Astarion uses a shortbow: 1d6 + 4

import random

roll1 = random.randint(1,15)
roll2 = random.randint(1,15)
roll3 = random.randint(1,15)
roll4 = random.randint(1,15)
roll5 = random.randint(1,20)
resultroll1 = 0



#Party Dictionary Goes Here
partyDictionary = {
    "party1" : {
        "Health" : 12,
        "Armor" : 17,
        "Damage" : roll1 ,
        "attack modifier" : 3,
    },
"party2" : {
        "Health" : 10,
        "Armor" : 14,
        "Damage" : roll2,
        "attack modifier" : 7,
    },
    "party3" : {
        "Health" : 8,
        "Armor" : 14,
        "Damage" : roll3,
        "attack modifier" : 4,
    },
}


#Enemy Dictionary Goes Here
enemydict = {
    "enemy1":{
        "name":"jumboman",
        "damage":roll1 ,
        "Health" : 10,
        "Armor": 14,
        "attack modifier" : 3,
    },
    "enemy2":{
        "name":"godtree",
        "damage":roll2,
        "Health" : 14,
        "Armor": 14,
        "attack modifier" : 5,
    },
    "enemy3":{
        "name":"estopas",
        "damage":roll3,
        "Health" : 25,
        "Armor": 14,
        "attack modifier" : 4,
    },
}


#Combat Code Goes Here
import random

roll1 = random.randint(1,6)
roll2 = random.randint(1,6)
roll3 = random.randint(1,6)
roll6 = random.randint(1,20)


d20 = roll6

if enemydict["enemy1"]["attack modifier"] + d20 > partyDictionary["party1"]["Armor"]:
    print("enemy1 attack hits")
    if partyDictionary["party1"]["Health"] > 0:
        print("party1 is still alive")
        if partyDictionary["party1"]["attack modifier"] + d20 > enemydict["enemy1"]["Health"]:
            print("party1 attack hits, enemy1 health is")
            print(partyDictionary["party1"]["Damage"] - enemydict["enemy1"]["Health"])
        elif partyDictionary["party1"]["attack modifier"] + d20 < enemydict["enemy1"]["Health"]:
            print("party1 attack misses")
    elif enemydict["enemy1"]["attack modifier"] + d20 < partyDictionary["party1"]["Health"]:
        print("attack missed")
elif enemydict["enemy1"]["attack modifier"] + d20 < partyDictionary["party1"]["Armor"]:
    print("enemy1 attack missed")











