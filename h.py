import time
my_string = input()
reversed_string = my_string[::-1]
for my_string in reversed_string:
    time.sleep(0.4)
    print(reversed_string)