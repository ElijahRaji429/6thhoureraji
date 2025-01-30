#Name: Elijah Raji
#Class:6th hour
#Assinment:hw18
import random
#1. Import the "random" library and create a def function that prints "Hello World!"
def hellow_world():
    print("hellow world")

#2. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanbag = ["red","black","blue","green","pink"]
#3. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def grab_bag():
    bag = random.choice(beanbag)
    print(bag)
    grab()
#4. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def grab():
    question = input("Would like to grab a beanbag Y/N")
    if question == "Y":
        grab_bag()
    elif question == "N":
        exit()

#5. Call the #3 function at the bottom.
grab_bag()
