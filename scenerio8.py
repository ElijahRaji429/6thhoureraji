#Name: Elijah Raji
#Class:6th hour
#Assinment:scenerio8

import random

#Scenario 8:
#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#(Translation: Rebuild Scenario 3 using classes instead of dictionaries, include the combat test code
#below as well.)

class Character:
    def __init__(self, health, damage, AC, attack_modifier):
        self.health = health
        self.damage = damage
        self.AC = AC
        self.attack_modifier =attack_modifier

party1 = Character(12, random.randint(1,6) + random.randint(1,6), 17,3)
party2 = Character(10, random.randint(1,6), 14,2)
party3 = Character(8, random.randint(1,6), 14,0)
party4 = Character(10, random.randint(1,6), 14,4)

enemy1 = Character(10, random.randint(1,11) + random.randint(1,6), 14,5)
enemy2 = Character(10, random.randint(1,11) + random.randint(1,6), 14, 5)
enemy3 = Character(10,random.randint(1,12) + random.randint(1,6) + random.randint(1,6), 14, 5)
enemy4 = Character(10, random.randint(1,9), 14,5)
enemy5 = Character(10, random.randint(1,8), 14,5)

partyattackRoll = random.randint(1,20) + party1.attack_modifier
if enemy1.AC < partyattackRoll:
    enemy1.health -= party1.damage
    print("attack hits, enemy health is", enemy1.health)
    if enemy1.health <=0:
        print("enemy os dead")
        exit()
    else:
        print("enemy id alive")
else:
    print("attack misses")

enemyattackRoll = random.randint(1,20) + enemy1.attack_modifier
if party1.AC < enemyattackRoll:
    party1.health -= enemy1.damage
    print("attack hits, party1 health is", party1.health)
    if party1.health <=0:
        print("party1 is dead")
        exit()
    else:
        print("party1 id alive")
else:
    print("attack misses")




