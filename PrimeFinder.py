#Prime finder, using module

import primes

print("I am a program to give you a list of primes that are less than a number")
print("Please give me a positive integer ('7', not 'seven')")
test = False
while test == False:
    try:
        number = int(input())
    except:
        print("That is not right")
    if number <= 0:
        print("Please give me a positive integer")
    elif number//1 != 0:
        print("Please give me an integer")
primelist = primes.primeFinder(number)
#print(primes.primeFinder(number))
print(primelist)
print("thank you")
