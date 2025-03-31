#Name: Elijah Raji
#Class:6th hour
#Assinment:hw23

import random, time

#1. Copy over your class from HW23 and all the functions inside of it, and alter any functions to use self if applicable.
class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed

    def take_damage(self):
        for i in range(10):
            damage_taken = random.randint(1,6)
            self.health -= damage_taken
            print(f"character takes {damage_taken} damage. New health: {self.health}")
            time.sleep(1)
#2. Create a fourth attribute in the class called max_health that has the same values as health
    def heal(self, target):
        heal_amount = 30
        target.health += heal_amount
        if target.health > 100:
            target.health = 100

#3. Copy the warrior and healer objects from HW23, and then make two more character objects with the following attribute values: thief (health/max: 50, damage: 30, speed: 40) and mage (health/max: 45, damage:35, speed: 25)
warrior = Character(100, 20, 30)
theif = Character(100, 20, 30)
healer = Character(100, 20, 30)
mage = Character(100, 20, 30)
#4. Randomly choose one of the four character objects to take the damage over time function and call the function to them
randomchoice = random.randint(1,4)
if randomchoice ==1:
    warrior.take_damage()
elif randomchoice ==2:
    healer.take_damage()
elif randomchoice ==3:
    theif.take_damage()
elif randomchoice ==4:
    mage.take_damage()
#5. Determine who lost health by comparing the current health to the max_health and heal that character object by calling your healing function to that object and then print their health afterwards.
