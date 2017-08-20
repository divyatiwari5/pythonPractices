l = list()
print("(Press enter twice once done)")
inp = int(input("Enter item: "))
while inp:
    l.append(inp)
    try:
        inp = int(input("Enter item: "))
    except ValueError:
        break

o = [x for x in l if x < 5]

print(o)
