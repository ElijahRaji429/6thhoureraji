#Name: Elijah Raji
#Class:6th hour
#Assinment:hw15
import random
#1. Create a def function that prints out "Hello World!"
def hello_world():
    print("Hello World!")


#2. Create a def function that calculates the average of three numbers.
def  calculate_average(z,y,x):
   a = z+y+x
   print(a/3)


#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.
def animal_list(*animal):
    print("The 3rd animals name is", animal[1])


#4. Create a def function that loops from 1 to the number put in the argument.
def numb_loop():
    for i in range(1,13):
        print(i)


#5. Call all of the functions created in 1 - 4 with relevant arguments.
