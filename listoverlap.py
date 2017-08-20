a = list()
b = list()

print("Enter items for list 1. Press Enter twice when done.")
current = input("Enter item: ")
while current:
    a.append(current)
    current = input("Enter item: ")


print("Enter items for list 2. Press Enter twice when done.")
current = input("Enter item: ")
while current:
    b.append(current)
    current = input("Enter item: ")

print(a)
print(b)
print(set(b) & set(a))

