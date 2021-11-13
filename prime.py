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
        if s*s > n:
            return True
        if n % s == 0:
            return False
    return True

def primes(z):
    r = []
    for i in range(2, z+1):
        if _check_prime(i, r):
            r += [i]
    return r

def primes_sqrt(z):
    r = []
    i = 2
    while i*i <= z:
        if _check_prime(i, r):
            r += [i]
        i += 1
    return r

def primes2(z):
    r = []
    for i in range(2, z+1):
        divisible = any((i % prime == 0 for prime in r))
        if not divisible:
            r += [i]
    return r

digit_superscript = {
    '0': '⁰',
    '1': '¹',
    '2': '²',
    '3': '³',
    '4': '⁴',
    '5': '⁵',
    '6': '⁶',
    '7': '⁷',
    '8': '⁸',
    '9': '⁹',
}

def superscript(x):
    return ''.join((digit_superscript.get(ch, ch) for ch in str(x)))

def primefactors(x):
    r = []
    for prime in primes_sqrt(x):
        power = 0
        while x % prime == 0:
            x //= prime
            power += 1
        if power != 0:
            r += [(prime, power)]
    if r == [] or x != 1:
        r += [(x,1)]
    return r

def powstr(base, power):
    if power == 1:
        return str(base)
    else:
        return "{}{}".format(base, superscript(power))

def primefactors_str(x):
    if x == 0:
        return "0"
    elif x < 0:
        return "-1·"+primefactors_str(-x)
    return '·'.join((powstr(prime, power) for (prime, power) in primefactors(x)))

def print_primefactors(x):
    print("{} = {}".format(x, primefactors_str(x)))

print(primes(200))

for i in range(16):
    print_primefactors(2**i-1)
print_primefactors(1024)

