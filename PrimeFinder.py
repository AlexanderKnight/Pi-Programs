#Prime finder, using module

import primes

print("Please give me a number")
number = int(input())
primelist = primes.primeFinder(number)
#print(primes.primeFinder(number))
print(primelist)
print("thank you")
