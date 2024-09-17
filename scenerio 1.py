#Name: ELijah Raji
#Class:6th hour
#Assinment:scenerio 1

enemydict = {
    "enemy1":{
        "name":"jumboman",
        "damage":12
    },
    "enemy2":{
        "name":"godtree",
        "damage":14
    },
    "enemy3":{
        "name":"estopas",
        "damage":36
    },
    "enemy4":{
        "name":"thatree",
        "damage":39
    },
    "enemy5":{
        "name":"thedoctor",
        "damage":52
    }
}
print(enemydict)

enemydict["enemy1"]["damage"] = (int(input()))
enemydict["enemy2"]["damage"] = (int(input()))
enemydict["enemy3"]["damage"] = (int(input()))
enemydict["enemy4"]["damage"] = (int(input()))
enemydict["enemy5"]["damage"] = (int(input()))

print(enemydict)