def smallest_true_divisor(n):
    if n < 2:
        return 1
    i = 2
    while i*i <= n:
        if n%i == 0:
            return i
        i += 1
    return 1

def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def _check_prime(n, sm):
    for s in sm:
        if n % s == 0:
            return False
        if s*s > n:
            return True
    return True

def primes(z):
    r = []
    for i in range(2, z+1):
        if _check_prime(i, r):
            r += [i]
    return r

def primes2(z):
    r = []
    for i in range(2, z+1):
        divisible = any((i % prime == 0 for prime in r))
        if not divisible:
            r += [i]
    return r
        

print(smallest_true_divisor(5))
print(smallest_true_divisor(77))
print(smallest_true_divisor(49))
print(primes(200))
