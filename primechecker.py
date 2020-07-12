def isPrime(n):
    if n < 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    else: # this else is matching with for loop, how it works?
        return True


isPrime = isPrime(97)
if isPrime:
    print('given number is prime')
else:
    print('given number is not prime')
