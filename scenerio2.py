#Name: ELijah Raji
#Class:6th hour
#Assinment:scenerio 2

partyDictionary = {
    "LaeZel" : {
        "Race" : "Githyanki",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "Health" : 12,
        "AC" : 17,
        "Damage" : 10,
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "Health" : 10,
        "AC" : 14,
        "Damage" : 5,
    },
    "Gale" : {
        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "Health" : 8,
        "AC" : 14,
        "Damage" : 17,
    },
    "Astarion" : {
        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "Health" : 10,
        "AC" : 14,
        "Damage" : 12,
    }
}
enemydict = {
    "bob" : {
        "race" : "human" ,
        "class" : "warrior" ,
        "background" : "the strongest",
        "health" : 100000 ,
        "ac" : 5000 ,
        "Damage" : 50000
    }
}

y = partyDictionary["Gale"]["Damage"]
x = enemydict["bob"]["health"]
z = y - x
print(z)