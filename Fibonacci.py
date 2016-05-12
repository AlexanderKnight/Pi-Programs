import numpy as np
#import matplotlib.pyplot as plt

def fib(N):
    '''
    Defines the first N fibonacci numbers
    '''
    n=[0,1]
    for i in range(N-2):
        n.append(n[i]+n[i+1])

    return n

def prime(N):
    '''
    Shows primes smaller than N
    '''
    
    primesCheck = np.ones(N-1)

    for i in range(1,N):
        if i == 1:
            primesCheck[i]=0
        if primesCheck[i]==1:
            for k in range(i**2, N//i):
                primesCheck[i*k] = 0

    primes =[]
    for i in range(1,N):
        if primesCheck[i] == 1:
            primes.append(i)

    return primes


def HelloWorld():
    print("Hello World!")




print("hello world")
