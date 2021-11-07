
v = ['Zénó', 'Aladár', 'Dezső', 'Géza', 'Ferenc', 'Péter', 'Balázs']

print(v)

# i, j = 0, len(v)-1

# while i < j:
#     v[i], v[j] = v[j], v[i]
#     i += 1
#     j -= 1

sorted = False
while not sorted:
    sorted = True
    for i in range(0, len(v)-1):
        if v[i] > v[i+1]:
            v[i], v[i+1] = v[i+1], v[i]
            sorted = False

print(v)