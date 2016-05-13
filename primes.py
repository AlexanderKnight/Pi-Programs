import numpy as np
class primes:
    def __init__():
        self.primes=[]
        self.length = len(self.primes)
    def primeFinder(self,N):
        primeCheck = np.ones(N+1)

        for i in range(2,N+1):
            if primeCheck[i] == 1:
                for j in range(i**2, N+1//i, i):
                    primeCheck[j]=0

        for i in range(2,N+1):
            if primeCheck[i]==1:
                self.primes.append(i)
        return self.primes
                               
