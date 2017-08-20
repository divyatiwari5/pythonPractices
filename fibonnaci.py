a = 0
b = 1
print(a, end=" ")
print(a+b, end=" ")
for i in range (6):
    c = a+b
    print(c, end=" ")
    a = b
    b = c

