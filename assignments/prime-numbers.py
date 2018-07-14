#Marvin Estime

def isPrime(n):
    if n < 2:
        return False
    for c in range(2, n):
        if n%c == 0:
            return False
    return True

#Problem #1
def showLowerPrimes(n):
    for c in range(2,n+1):
        if isPrime(c):
            print(c)

#Problem #2
def showPrimeFactorization(n):
    for c in range (2, n+1):
        if n%c == 0:
            if isPrime(c):
                print(c)

#Problem #3
def gradeToLetter(n):
    if n >= 90:
        print("A")
    elif n >= 80:
         print("B")
    elif n >= 70:
        print("C")
    elif n >= 65:
        print("D")
    else:
        print("F")

def collatz(n):
    print(n)
    while n > 1:
        if n % 2 == 0:
            n/=2
        else:
            n = 3*n + 1
        print(n)

showLowerPrimes(int(input("Give me a number, and I'll tell you the primes less/equal to it\n")))
showPrimeFactorization(int(input("Give me another number and I'll show you the prime factorization\n")))
gradeToLetter(int(input("Tell me your grade and I'll onvert it for you\n")))
collatz(int(input("Give me a number, and I'll produce the collatz conjecture")))