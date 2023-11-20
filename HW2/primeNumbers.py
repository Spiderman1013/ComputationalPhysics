import math

def is_prime(n, primes):
    for prime in primes:
        if prime > math.isqrt(n):
            break
        if n % prime == 0:
            return False
    return True


def main():
    primeNumbers = [2]
    limit = 10000
    #Don't need to check even numbers
    for i in range(3, limit+1, 2):
        if is_prime(i, primeNumbers):
            primeNumbers.append(i)
    
    for prime in primeNumbers:
        print(prime)

if __name__ == "__main__":
    main()