#Name: Elijah Raji
#Class:6th hour
#Assinment:scenerio7

import Scenerio6
from Scenerio6 import characterlist

listAverage = 0

def final_average():
    global listAverage
    listAverage = sum(characterlist)/len(characterlist)
    return listAverage

final_average()

print(listAverage)