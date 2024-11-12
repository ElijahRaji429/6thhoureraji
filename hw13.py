#Name: Elijah Raji
#Class:6th hour
#Assinment:hw13
from itertools import count

#1. Create a list containing 10 integers of your choice.
numlist = [2,4,6,7,35,75,23,54,76,1]
#2. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers = 0
oddNumbers = 0
#3. Make a loop that counts the number of even and odd numbers in the list.
#(HINT: The way to see if a number is even is if it is divisible by 2).
for i in numlist:
    if i % 2 == 0:
        evenNumbers += 1
    else:
        oddNumbers += 1


# Print the total count of even and odd numbers.
print(evenNumbers)
print(oddNumbers)