#Name: Elijah Raji
#Class:6th hour
#Assinment:hw17


#1. Import the "random" library and create a def function that prints "Hello World!"

#2. Create two empty integer variables named "heads" and "tails"

#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.

#4. Call the "Hello world" and "Coin Flip" functions here

#5. Print the final result of heads and tails here
import random
def hello_world():
    print("Hello World!")



heads = 0
tails = 0
def flip_coin():
    global heads
    global tails
    for i in range(1,101):
        coin_flip = random.randint(1,2)
        if coin_flip == 2:
            heads += 1
        else:
            tails += 1

hello_world()
flip_coin()

print(heads)
print(tails)
