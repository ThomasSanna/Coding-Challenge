# Ecrire un programme qui trouve tous les nombres premiers
# inférieurs à un nombre > 0 donné en utilisant le crible d'Eratosthène.

# Write a program that finds all prime numbers
# less than a given > 0 number using the Sieve of Eratosthenes.


def cribleEratosthene(n):
    if n==1:
        return 1
    
    else:
        arrNotPrimes = [1]
        arrPrimes = [i for i in range (2, n+1)]
        index = 0
        active = True
        
        while active:
            for j in range (arrPrimes[index], n):
                if (j!=arrPrimes[index] and j%arrPrimes[index]==0):
                    arrNotPrimes.append(j)
            for k in range (len(arrNotPrimes)):
                while arrNotPrimes[k] in arrPrimes:
                    arrPrimes.remove(arrNotPrimes[k])
            index += 1
            if index+1 == len(arrPrimes):
                if (arrPrimes[index]%arrPrimes[index-1]!=0):
                    arrPrimes.remove(arrPrimes[index])
                active = False
        return arrPrimes

print(cribleEratosthene(100))

# BOT SOLUTION

def cribleEratosthene2(n):
    arrPrimes = list(range(2, n+1))
    for i in arrPrimes:
        arrPrimes = list(filter(lambda x: x == i or x % i != 0, arrPrimes))
    return arrPrimes

print(cribleEratosthene2(100))