#Name: Elijah Raji
#Class:6th hour
#Assinment:hw12

#1. Create a for loop with variable i that counts down from 5 to 1
#and then prints "Hello World!" at the end.
import time
for i in range(5,0,-1):
    time.sleep(0.4)
    print(i)
else:
    print("hello world")

#2. Create a for loop that counts up and prints only even numbers
#between 1 and 30.
#(HINT: Look back to HW6 on how to see if a number is divisible by another)
for i in range(2,32,2):
    time.sleep(0.4)
    print(i)

#3. Create a for loop that prints 5 different animals from a list.
animal = ["monkey", "tiger", "zebra", "lion", "elephant"]
for y in animal:
    time.sleep(0.4)
    print(y)

#4. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
for z in input("Give me a word: ")[::-1]:
    print(z)