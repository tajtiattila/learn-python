for i in range(1,100):
    s = ""
    if i % 3 == 0:
        s = "fizz"
    if i % 5 == 0:
        s += "buzz"
    if s == "":
        s = i
    print(s)
