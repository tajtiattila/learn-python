print("Think of a number n so that 0 <= n <= 100.")
print("I try to guess your number.")

nlo = 0
nhi = 100
nsteps = 0
while nlo < nhi:
    m = int((nlo+nhi)/2)
    print("My guess is: {}".format(m))
    nsteps += 1

    ansvalid = False
    while not ansvalid:
        ans = input("Is you number (s)maller, (l)arger or (e)qual? ")
        if ans == 's':
            nhi = m - 1
            ansvalid = True
        elif ans == 'l':
            nlo = m + 1
            ansvalid = True
        elif ans == 'e':
            nlo, nhi = m, m
            ansvalid = True
        else:
            print("Invalid answer!")

print("Your number was {}. I guessed it in {} steps.".format(nlo, nsteps))