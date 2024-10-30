#Name: Elijah Raji
#Class:6th hour
#Assinment:hw11
import time

#A common exercise in computer science is "FizzBuzz". The rules of
#the game are simple. Count from 1 to 100 but with every number that
#is divisible by 3 you say "Fizz" instead of the number,
#every number divisible by 5 you say "Buzz" instead,
#and if it's divisible by both you say "FizzBuzz".

#Create a while loop that follows the rules of the game.
#(HINT: Look back to HW6 on how to see if a number is divisible by another)
i = 0
while i <= 100:
    print(i)
    time.sleep(0.4)
    i += 1
    if i % 3==0:
        ("fizz")
    #elif i % 5==0:
     #   print("buzz")
    #elif i % 3==0 and i % 5==0:
       # print("fizzbuzz")

