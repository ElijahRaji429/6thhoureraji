#Name: Elijah Raji
#Class:6th hour
#Assinment:hw14

#1. Create a variable that asks the user for an integer and an empty intger variable.
a = int(input())
b = 1

#2. Create a loop with a range from 1 to the number the user input.
for c in range(1,a+1):

#3. Use the loop to find the factorial of that number. A factorial of a number is that number multiplied
#by every number before it until you reach 1.
#For example: 5! is 5 x 4 x 3 x 2 x 1 = 120
    b *=c

#4. Print the factorial.
print(b)