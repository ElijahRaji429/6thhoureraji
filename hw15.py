#Name: Elijah Raji
#Class:6th hour
#Assinment:hw15
import random
#1. Create a def function that prints out "Hello World!"
def hello_world():
    print("Hello World!")

hello_world()
#2. Create a def function that calculates the average of three numbers.
def  calculate_average(z,y,x):
   a = z+y+x
   print(a/3)
calculate_average(3,5,6)

#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.
def animal_list(*animal):
    print("The 3rd animals name is", animal[1])
animal_list("dog","cat","fish","parrot","monkey")

#4. Create a def function that loops from 1 to the number put in the argument.
def numb_loop():
    for i in range(1,13):
        print(i)
numb_loop()

#5. Call all of the functions created in 1 - 4 with relevant arguments.
numb_loop()
animal_list("dog","cat","fish","parrot","monkey")
calculate_average(3,5,6)
hello_world()