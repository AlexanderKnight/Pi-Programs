import numpy as np
def primeFinder(N):
    primes = []
    primeCheck = np.ones(N+1)
    for i in range(2,N+1):
        if primeCheck[i] == 1:
            for j in range(i**2, (N+1//i)+1, i):
                primeCheck[j]=0

    for i in range(2,N+1):
        if primeCheck[i]==1:
            primes.append(i)
    return primes
                               
