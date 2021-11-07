print("Guess my number between 0 and 100!")

nmin = 0
nmax = 100

nsteps = 0
while True:
    n = int(input("Your guess: "))
    if n < 0 or n > 100:
        print("Invalid guess, must be between 0 and 100.")
        continue
    nsteps += 1
    if n == nmin and n == nmax:
        break
    mid = (nmin+nmax)/2
    if n > mid:
        print("My number is smaller.")
        if n <= nmax:
            nmax = n-1
    else:
        print("My number is larger.")
        if n >= nmin:
            nmin = n+1

print("Correct, my number was {}. You guessed {} times.".format(nmin, nsteps))