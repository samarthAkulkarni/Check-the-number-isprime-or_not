def isPrime(num):
    not_prime = False
    for i in range(2, num):
        if num % i == 0:
            not_prime = True
        
    
    if not_prime:
        return False
    else:
        return True
