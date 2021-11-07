print("Think of a number n so that 0 <= n <= 100.")
print("I try to guess your number.")

def get_answer(guess: int):
    print("My guess is: {}".format(guess))
    while True:
        ans = input("Is you number (s)maller, (l)arger or (e)qual? ")
        if ans == 's' or ans == 'l' or ans == 'e':
            return ans
        else:
            print("Invalid answer!")

nlo = 0
nhi = 100
nsteps = 0
while nlo < nhi:
    m = int((nlo+nhi)/2)
    nsteps += 1

    ans = get_answer(m)
    if ans == 's':
        nhi = m - 1
    elif ans == 'l':
        nlo = m + 1
    else:
        nlo, nhi = m, m

print("Your number was {}. I guessed it in {} steps.".format(nlo, nsteps))